# do = digital ocean
# pvc = private volume claim
# admin/iloveyou
#
# Digital Ocean affiliate signup link. Gives us both free credits https://m.do.co/c/f9d347ca9972

import os
import zipfile

cluster_vars = {
		"image_pull_secret_name"         : "docker-hub",
		"image_pull_secret"              : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==",
		"root_domain"                    : "quh.io",  # modify according to your domain/cluster name
		"load_balancer_name"             : "quh",  # modify according to your domain/cluster name
		"k8s_cluster_name"               : "quh",  # modify according to your domain/cluster name
		"k8s_context"                    : "do-nyc1-quh",  # modify according to your domain/cluster name
		"app1_name"                      : "app1",
		"sftp_k8s_pvc_name"              : "sftp-sftp-server-data",
		"docker_hub_registry"            : "kielerrr",  # use your dockerhub registry
		"k8s_root_dir"                   : "C:\\Users\\user_account\\.kube",
		"sftp_login_public_key"          : "AAAAB3NzaC1yc2EAAAADAQABAAAAgQCnF0poOWxSf+7z2XlbOzqUSakkrB8RFRa1wURjbWow3ETzOQzxcqAKuwb7ULSuC7usDl3VMgpWtpmBZyZpYJTkQ8w5PhdtJIR6PiDQw7Mq0X5bAO+GiT9PF+SEaBKSYsS730KzSF3xKHOh/swHOLhIk0HeD84ijGqieaMstRB5/Q==",
		"sftp_private_key_base64_encoded": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlDWEFJQkFBS0JnUUNuRjBwb09XeFNmKzd6MlhsYk96cVVTYWtrckI4UkZSYTF3VVJqYldvdzNFVHpPUXp4CmNxQUt1d2I3VUxTdUM3dXNEbDNWTWdwV3RwbUJaeVpwWUpUa1E4dzVQaGR0SklSNlBpRFF3N01xMFg1YkFPK0cKaVQ5UEYrU0VhQktTWXNTNzMwS3pTRjN4S0hPaC9zd0hPTGhJazBIZUQ4NGlqR3FpZWFNc3RSQjUvUUlEQVFBQgpBb0dBRmhBTHVaNVhjTDlHd0hrSFBxWWY4b09WYTJ1MHdHOHQ2L3JrZWxKd3NwbnJHc2grTG9WcG4zRVpsMmFOCkxPd01zRWZIV1FhOStid3JvYndLaE9DRldEV04rMFZidmRwb0l0bHJMNTFaenNRVVZuTXF3L2pqZ0U0MGdrVzUKZk4rbmx4SjRnVnFHSnhkSGljQ0tmYU5PalFzbG1NZVNKUVppdW8wc3U3WGtoK3NDUVFDMXRzM2FTT0UxSTQ0TgpRdVRra0JUVWQ4K25yR3RBWTk0cG5UbnBrNldJYXpmc3dKT3djeXViRWNNL3RudkN3by8xaHdUcWNsT2lkbzBqCmYyZWZRMlNQQWtFQTYyWWRCelhjUTdFT2RpNEVlQm13a0tUSS9FNEJBbzJTWmZheEVWTkpha251M0NRVlBRV1oKdGpCVTdnYWRXWlZ5UnBaNlJGbDM1TFd0MDdaOS9oVTJzd0pBYTVFU0hIUmw5RG5lM2hUS1FFN1dOY3ZTdmRRQQpEVGJSRFZ0SUsrKzkzcHB4bVpHS0c3cWhob01tVEhIdW95VGZhUjJMR0dtaS9wb2xCRzFuM3N4Ykd3SkFQa0hxCmlYNm9POHIzTFRCc2hDc2ZOSkl3aWZKRGVCNWpTczVjOUYwWHZLSERKN3Z2VmcxR0l4WlRVQVMxMXZ5Y2xhaTAKdTZFQ0FaNC9WQkFlOEhWQjJ3SkJBSldrZ1dOK1ZTaktLZDV5RERub0RSWGZnSUt6d1VBeVI2VU5nUW1XUWIwTwpXQm5GL2IrMlg4dlhtZXI1QnVMdHRoczlBMDJIeC94M3FxTEpxL1dSS2lRPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ==",
		"sftp_size"                      : "25Gi",
		"sftp_uid"                       : "1000",
		"sftp_gid"                       : "100",
		"storage_class"                  : "do-block-storage",  # default for do. change if not using do
		"dns_challenge_provider"         : "digitalocean",
		"external_ip"                    : "1.2.3.4",  # use external ip that populates in the loadbalancer after it is created.
		"traefik_pvc_size"               : "5Gi",
		"webauth_secret"                 : "YWRtaW46JGFwcjEkMmVpczQzbnUkQ0w4YXlMRlMwMExkWEZLbkdyRzI3Lw==",  # admin/iloveyou
		"do_auth_token_name"             : "do-auth-token",
		"do_auth_token_value"            : "aWxvdmV5b3U=",  # this is a dummy value, if using digital ocean, add this to connecct lb and volumes
		"rate_limit_avg"                 : "100",
		"rate_limit_burst"               : "500",
		"grafana_user"                   : "YWRtaW4==",  # admin
		"grafana_password"               : "aWxvdmV5b3U=",  # iloveyou
		"grafana_password_plain"         : "iloveyou",
		"grafana_volume_size"            : "10Gi"
		}

SEARCH_DIR = '.'
BACKUP_DIR = '../'


def get_list_of_files(starting_dir):
	list_of_files = os.listdir(starting_dir)
	all_files = []
	for entry in list_of_files:
		if 'node_modules' not in entry:
			full_path = os.path.join(starting_dir, entry)
			if os.path.isdir(full_path):
				all_files = all_files + get_list_of_files(full_path)
			else:
				if 'node_modules' not in full_path:
					all_files.append(full_path)
	
	return all_files


def replace_lines(file_before):
	fixed_lines = []
	loaded_file = open(file_before, 'r')
	loaded_file_content = loaded_file.readlines()
	
	for line in loaded_file_content:
		for var in cluster_vars:
			search_str = "{{{{ " + var + " }}}}"
			if search_str in line:
				line = line.replace(search_str, cluster_vars[var])
		fixed_lines.append(line)
	
	loaded_file = open(file_before, 'w')
	loaded_file.writelines(fixed_lines)
	return loaded_file.close()


def main():
	ignore_files = ['node_modules', '.idea', '.vscode', '.git']
	zf = zipfile.ZipFile(f'{BACKUP_DIR}theme_backup.zip', 'w')
	list_of_files = []
	for (dirpath, dirnames, filenames) in os.walk(SEARCH_DIR):
		list_of_files += [os.path.join(dirpath, file) for file in filenames]
	
	# Print the files
	for elem in list_of_files:
		zf.write(elem)
	zf.close()
	
	list_of__liquid_files = get_list_of_files(SEARCH_DIR)
	for elem in list_of__liquid_files:
		try:
			if 'node_modules' not in elem:
				replace_lines(elem)
		except:
			print(f'not processed file: {elem}')


if __name__ == '__main__':
	main()
