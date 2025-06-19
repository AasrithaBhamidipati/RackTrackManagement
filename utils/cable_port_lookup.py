import csv
import os
import logging

def get_cable_port_connections(cable_name):
    """
    Look up port connections for a given cable name
    
    Args:
        cable_name (str): Name of the cable to look up
        
    Returns:
        dict: Dictionary with port1 and port2 connections, or None if not found
    """
    try:
        # Check for available data files (prefer CSV for reliability, fallback to Excel)
        csv_file = "cables-ports.csv"
        excel_files = ["Cables-ports 1.xlsx", "Cables-ports.xlsx"]
        
        data_file = None
        file_type = None
        
        # Check for CSV file first (more reliable)
        if os.path.exists(csv_file):
            data_file = csv_file
            file_type = 'csv'
        else:
            # Fallback to Excel files
            for excel_file in excel_files:
                if os.path.exists(excel_file):
                    data_file = excel_file
                    file_type = 'excel'
                    break
        
        if not data_file:
            logging.warning(f"Cable-port mapping file not found")
            return None
        
        # Read the data file
        if file_type == 'excel':
            try:
                # Try to import pandas dynamically
                import pandas as pd
                df = pd.read_excel(data_file)
                # Find exact or partial match
                matches = df[df['Name'].str.strip().str.lower() == cable_name.strip().lower()]
                
                if not matches.empty:
                    row = matches.iloc[0]  # Get first match
                    return {
                        'port1': str(row['Port 1']).strip(),
                        'port2': str(row['Port 2']).strip(),
                        'cable_name': str(row['Name']).strip()
                    }
            except ImportError:
                logging.warning(f"pandas not available, cannot read Excel file {data_file}")
                return None
            except Exception as e:
                logging.error(f"Error reading Excel file {data_file}: {str(e)}")
                return None
                
        elif file_type == 'csv':
            with open(data_file, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['Name'].strip().lower() == cable_name.strip().lower():
                        return {
                            'port1': row['Port 1'].strip(),
                            'port2': row['Port 2'].strip(),
                            'cable_name': row['Name'].strip()
                        }
            
        logging.info(f"No port connections found for cable: {cable_name}")
        return None
            
    except Exception as e:
        logging.error(f"Error looking up cable port connections: {str(e)}")
        return None

def format_cable_port_info(port_info):
    """
    Format cable port information for display
    
    Args:
        port_info (dict): Port connection information
        
    Returns:
        str: Formatted HTML string for display
    """
    if not port_info:
        return ""
    
    return f"""
    <div class="mt-3 p-3 bg-light rounded">
        <h6 class="text-info mb-2">
            <i class="fas fa-plug me-1"></i>Port Connections
        </h6>
        <div class="row text-center">
            <div class="col-6">
                <div class="h6 mb-0 text-primary">{port_info['port1']}</div>
                <small class="text-muted">Port 1</small>
            </div>
            <div class="col-6">
                <div class="h6 mb-0 text-primary">{port_info['port2']}</div>
                <small class="text-muted">Port 2</small>
            </div>
        </div>
        <div class="text-center mt-2">
            <small class="text-muted">
                <i class="fas fa-arrows-alt-h me-1"></i>
                {port_info['port1']} ↔ {port_info['port2']}
            </small>
        </div>
    </div>
    """