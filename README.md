# Azure-Storage-Account
How to connect python app to blob Storage in Azure 
In the first part ,you need to import the libraries azure.storage.blob
than create a connection string ,you could use the command 
"az storage account show-connection-string \
  --resource-group learn-7d42e66a-f536-437e-95f3-667a608b59cb \
  --query connectionString \
  --name <name>"
  the command gonna return a string that you will use to craete a global variable 
  
