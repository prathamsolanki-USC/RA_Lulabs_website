import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    Main Lambda function handler for genomic data queries
    """
    try:
        # Parse the incoming request
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        
        # Handle different endpoints
        if path == '/api/query' and http_method == 'POST':
            return handle_query_request(event)
        elif path == '/api/health' and http_method == 'GET':
            return handle_health_check()
        elif path == '/' and http_method == 'GET':
            return handle_home_page()
        else:
            return create_response(404, {'error': 'Endpoint not found'})
            
    except Exception as e:
        print(f"Error in lambda_handler: {str(e)}")
        return create_response(500, {'error': 'Internal server error'})

def handle_query_request(event):
    """
    Handle genomic data query requests
    """
    try:
        # Parse request body
        body = event.get('body', '{}')
        if isinstance(body, str):
            data = json.loads(body)
        else:
            data = body
            
        # Extract query parameters
        selections = data.get('selections', {})
        files_required = data.get('files_required', [])
        limit = data.get('limit', 100)
        include_download = data.get('include_download', False)
        
        # Validate required fields
        if not selections:
            return create_response(400, {'error': 'No selections provided'})
            
        if not files_required:
            return create_response(400, {'error': 'No files required specified'})
        
        # Generate SQL query (same logic as Django)
        sql_query = generate_sql_query(selections, limit)
        
        # Mock response for now (replace with actual database query)
        result = {
            'success': True,
            'query_id': f'query_{int(datetime.now().timestamp())}',
            'sql_query': sql_query,
            'selections': selections,
            'files_required': files_required,
            'limit': limit,
            'include_download': include_download,
            'results': [
                {
                    'id': 1,
                    'species': selections.get('species', 'Unknown'),
                    'cell_type': selections.get('cell_type', 'Unknown'),
                    'crosslinker': selections.get('crosslinker', 'Unknown'),
                    'litigation_time': selections.get('litigation_time', {}).get('value', 'Unknown'),
                    'files': files_required
                }
            ],
            'message': 'Query executed successfully'
        }
        
        return create_response(200, result)
        
    except json.JSONDecodeError:
        return create_response(400, {'error': 'Invalid JSON data'})
    except Exception as e:
        print(f"Error in handle_query_request: {str(e)}")
        return create_response(500, {'error': f'Query processing error: {str(e)}'})

def generate_sql_query(selections, limit):
    """
    Generate SQL query based on selections (same logic as Django)
    """
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
    
    return sql_query

def handle_health_check():
    """
    Health check endpoint
    """
    return create_response(200, {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Genomic Data Query Lambda'
    })

def handle_home_page():
    """
    Home page endpoint
    """
    return create_response(200, {
        'message': 'Welcome to Genomic Data Query Interface',
        'endpoints': {
            'query': '/api/query (POST)',
            'health': '/api/health (GET)',
            'home': '/ (GET)'
        },
        'timestamp': datetime.now().isoformat()
    })

def create_response(status_code, body):
    """
    Create standardized API Gateway response
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
        },
        'body': json.dumps(body, default=str)
    }
