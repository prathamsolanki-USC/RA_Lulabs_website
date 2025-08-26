import json
import time
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
import os
from dotenv import load_dotenv

load_dotenv()

def home(request):
    """Home page view"""
    return render(request, 'query_interface/home.html')

def query_view(request):
    """Query interface page view"""
    return render(request, 'query_interface/query.html')

def results_view(request):
    """Results display page view"""
    return render(request, 'query_interface/results.html')

def documentation_view(request):
    """Documentation page view"""
    return render(request, 'query_interface/documentation.html')

@csrf_exempt
@require_http_methods(["POST"])
def api_query(request):
    """Handle API queries and integrate with external file download API"""
    try:
        # Parse request data
        data = json.loads(request.body)
        
        # Extract query parameters
        selections = data.get('selections', {})
        files_required = data.get('files_required', [])
        limit = data.get('limit', 100)
        include_download = data.get('include_download', False)
        access_key = data.get('access_key', '')
        secret_key = data.get('secret_key', '')
        
        # Log the received data for debugging
        print(f"=== API QUERY RECEIVED ===")
        print(f"Selections: {selections}")
        print(f"Files Required: {files_required}")
        print(f"Limit: {limit}")
        print(f"Include Download: {include_download}")
        
        # Validate required fields
        if not selections:
            return JsonResponse({
                'success': False,
                'error': 'No selections provided'
            }, status=400)
        
        if not files_required:
            return JsonResponse({
                'success': False,
                'error': 'No files required specified'
            }, status=400)
        
        # Generate dynamic SQL query based on actual selections
        sql_conditions = []
        
        if selections.get('species'):
            sql_conditions.append(f"species = '{selections['species']}'")
        
        if selections.get('cell_type'):
            sql_conditions.append(f"cell_type = '{selections['cell_type']}'")
        
        if selections.get('crosslinker'):
            sql_conditions.append(f"crosslinker = '{selections['crosslinker']}'")
        
        if selections.get('ligase'):
            sql_conditions.append(f"ligase = '{selections['ligase']}'")
        
        if selections.get('extra'):
            sql_conditions.append(f"extra = '{selections['extra']}'")
        
        # Handle numeric fields with operators
        if 'litigation_time' in selections:
            op = selections['litigation_time'].get('operator', '=')
            val = selections['litigation_time'].get('value', '')
            if val:
                sql_conditions.append(f"litigation_time {op} {val}")
        
        if 'ligation_incubation_time' in selections:
            op = selections['ligation_incubation_time'].get('operator', '=')
            val = selections['ligation_incubation_time'].get('value', '')
            if val:
                sql_conditions.append(f"ligation_incubation_time {op} {val}")
        
        if 'exo_time' in selections:
            op = selections['exo_time'].get('operator', '=')
            val = selections['exo_time'].get('value', '')
            if val:
                sql_conditions.append(f"exo_time {op} {val}")
        
        # Build the WHERE clause
        where_clause = " AND ".join(sql_conditions) if sql_conditions else "1=1"
        
        # Generate the SQL query
        sql_query = f"SELECT * FROM cris_database.cris_table WHERE {where_clause} LIMIT {limit}"
        
        print(f"Generated SQL: {sql_query}")
        
        # Build the query payload for the external API
        query_payload = {
            'path': '/api/query',  # Required by Lambda for routing
            'selections': selections,
            'files_required': files_required,
            'limit': limit,
            'include_download': include_download,
            'access_key': access_key,
            'secret_key': secret_key
        }
        
        # Make request to external query API (your Lambda function)
        external_api_url = 'https://j3lvfct2qbqkyb7ix3tvratgde0gplda.lambda-url.us-east-2.on.aws/'
        
        print(f"Calling external API: {external_api_url}")
        print(f"Payload: {query_payload}")
        
        response = requests.post(
            external_api_url,
            json=query_payload,
            headers={'Content-Type': 'application/json'},
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"External API response: {result}")
            
            # Generate a query ID if the API doesn't provide one
            if not result.get('query_id'):
                result['query_id'] = f'query_{int(time.time())}'
                print(f"Generated query ID: {result['query_id']}")
            
            return JsonResponse(result)
        else:
            print(f"External API error: {response.status_code} - {response.text}")
            return JsonResponse({
                'success': False,
                'error': f'External API error: {response.status_code} - {response.text}'
            }, status=response.status_code)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Server error: {str(e)}'
        }, status=500)
