### Definition supports OCSF v1.5

OCSF_BASE = 'https://schema.ocsf.io/1.5.0/?extensions='

OCSF_BASE_EVENT = 'https://schema.ocsf.io/1.5.0/classes/base_event'

OCSF_OBJECTS = 'https://schema.ocsf.io/1.5.0/objects'

OCSF_DICTIONARY = 'https://schema.ocsf.io/1.5.0/dictionary'

OCSF_CATEGORIES = {
    'System Activity': 'https://schema.ocsf.io/1.5.0/categories/system',
    'Network Activity': 'https://schema.ocsf.io/1.5.0/categories/network',
    'Application Activity': 'https://schema.ocsf.io/1.5.0/categories/application',
    'Findings': 'https://schema.ocsf.io/1.5.0/categories/findings',
    'Discovery': 'https://schema.ocsf.io/1.5.0/categories/discovery',
    'Remediation': 'https://schema.ocsf.io/1.5.0/categories/remediation',
    'Unmanned Systems': 'https://schema.ocsf.io/1.5.0/categories/unmanned_systems',
    'Identity & Access Management': 'https://schema.ocsf.io/1.5.0/categories/iam'
}

OCSF_CLASSES = {
    'System Activity': {
        'File System Activity': 'https://schema.ocsf.io/1.5.0/classes/file_activity',
        'Kernel Extension Activity': 'https://schema.ocsf.io/1.5.0/classes/kernel_extension_activity',
        'Kernel Activity': 'https://schema.ocsf.io/1.5.0/classes/kernel_activity',
        'Memory Activity': 'https://schema.ocsf.io/1.5.0/classes/memory_activity',
        'Module Activity': 'https://schema.ocsf.io/1.5.0/classes/module_activity',
        'Scheduled Job Activity': 'https://schema.ocsf.io/1.5.0/classes/scheduled_job_activity',
        'Process Activity': 'https://schema.ocsf.io/1.5.0/classes/process_activity',
        'Event Log Activity': 'https://schema.ocsf.io/1.5.0/classes/event_log_actvity',
        'Script Activity': 'https://schema.ocsf.io/1.5.0/classes/script_activity'
    },
    'Network Activity': {
        'Network Activity': 'https://schema.ocsf.io/1.5.0/classes/network_activity',
        'HTTP Activity': 'https://schema.ocsf.io/1.5.0/classes/http_activity',
        'DNS Activity': 'https://schema.ocsf.io/1.5.0/classes/dns_activity',
        'DHCP Activity': 'https://schema.ocsf.io/1.5.0/classes/dhcp_activity',
        'RDP Activity': 'https://schema.ocsf.io/1.5.0/classes/rdp_activity',
        'SMB Activity': 'https://schema.ocsf.io/1.5.0/classes/smb_activity',
        'SSH Activity': 'https://schema.ocsf.io/1.5.0/classes/ssh_activity',
        'FTP Activity': 'https://schema.ocsf.io/1.5.0/classes/ftp_activity',
        'Email Activity': 'https://schema.ocsf.io/1.5.0/classes/email_activity',
        'NTP Activity': 'https://schema.ocsf.io/1.5.0/classes/ntp_activity',
        'Tunnel Activity': 'https://schema.ocsf.io/1.5.0/classes/tunnel_activity'
    },
    'Application Activity': {
        'Web Resources Activity': 'https://schema.ocsf.io/1.5.0/classes/web_resources_activity',
        'Application Lifecycle': 'https://schema.ocsf.io/1.5.0/classes/application_lifecycle',
        'API Activity': 'https://schema.ocsf.io/1.5.0/classes/api_activity',
        'Datastore Activity': 'https://schema.ocsf.io/1.5.0/classes/datastore_activity',
        'File Hosting Activity': 'https://schema.ocsf.io/1.5.0/classes/file_hosting',
        'Scan Activity': 'https://schema.ocsf.io/1.5.0/classes/scan_activity',
        'Application Error': 'https://schema.ocsf.io/1.5.0/classes/application_error'
    },
    'Findings': {
        'Vulnerability Finding': 'https://schema.ocsf.io/1.5.0/classes/vulnerability_finding',
        'Compliance Finding': 'https://schema.ocsf.io/1.5.0/classes/compliance_finding',
        'Detection Finding': 'https://schema.ocsf.io/1.5.0/classes/detection_finding',
        'Incident Handling': 'https://schema.ocsf.io/1.5.0/classes/incident_finding',
        'Data Security Finding': 'https://schema.ocsf.io/1.5.0/classes/data_security_finding',
        'Application Security Posture Finding': 'https://schema.ocsf.io/1.5.0/classes/application_security_posture_finding' 
    },
    'Discovery': {
        'Device Inventory Info': 'https://schema.ocsf.io/1.5.0/classes/inventory_info',
        'User Inventory Info': 'https://schema.ocsf.io/1.5.0/classes/user_inventory',
        'Operating System Patch State': 'https://schema.ocsf.io/1.5.0/classes/patch_state',
        'Device Config State Change': 'https://schema.ocsf.io/1.5.0/classes/device_config_state_change',
        'Software Inventory Info': 'https://schema.ocsf.io/1.5.0/classes/software_info',
        'OSINT Inventory Info': 'https://schema.ocsf.io/1.5.0/classes/osint_inventory_info',
        'Cloud Resources Inventory Info': 'https://schema.ocsf.io/1.5.0/classes/cloud_resources_inventory_info',
        'Live Evidence Info': 'https://schema.ocsf.io/1.5.0/classes/evidence_info'
    },
    'Remediation': {
        'Remediation Activity': 'https://schema.ocsf.io/1.5.0/classes/remediation_activity',
        'File Remediation Activity': 'https://schema.ocsf.io/1.5.0/classes/file_remediation_activity',
        'Process Remediation Activity': 'https://schema.ocsf.io/1.5.0/classes/process_remediation_activity',
        'Network Remediation Activity': 'https://schema.ocsf.io/1.5.0/classes/network_remediation_activity'
    },
    'Unmanned Systems': {
        'Drone Flights Activity': 'https://schema.ocsf.io/1.5.0/classes/drone_flights_activity',
        'Airborne Broadcast Activity': 'https://schema.ocsf.io/1.5.0/classes/airborne_broadcast_activity'
    },
    'Identity & Access Management': {
        'Account Change': 'https://schema.ocsf.io/1.5.0/classes/account_change',
        'Authentication': 'https://schema.ocsf.io/1.5.0/classes/authentication',
        'Authorize Session': 'https://schema.ocsf.io/1.5.0/classes/authorize_session',
        'Entity Management': 'https://schema.ocsf.io/1.5.0/classes/entity_management',
        'User Access Management': 'https://schema.ocsf.io/1.5.0/classes/user_access',
        'Group Management': 'https://schema.ocsf.io/1.5.0/classes/group_management'
    }
}