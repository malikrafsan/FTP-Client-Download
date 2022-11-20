import ftplib
import config
from timeit import default_timer as timer
import sys

def get_file(ftp_server: ftplib.FTP, file_server, file_client):
  print("<><><><><><><><><><><><><><><><><><><><><><>")
  print("Downloading file: " + file_server)
  start = timer()
  
  with open(file_client, "wb") as file:
    ftp_server.retrbinary(f"RETR {file_server}", file.write)
  
  end = timer()
  print(f"Downloaded in {end - start} seconds")
  print("<><><><><><><><><><><><><><><><><><><><><><>\n")
  
  return end - start

def main():
  ftp_server = ftplib.FTP(config.HOSTNAME, config.USERNAME, config.PASSWORD)
  ftp_server.encoding = "utf-8"

  files = config.FILES
  result = []
  for file in config.FILES:
    res = get_file(ftp_server, file, files[file])
    result.append(res)

  ftp_server.quit()

  N_client = sys.argv[1]
  with open(config.CSV_FILE, "a") as file:
    file.write(f"{N_client},{result[0]},{result[1]},{result[2]}\n")

if __name__ == '__main__':
  main()
