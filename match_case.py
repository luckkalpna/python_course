def https_status(status):
  match status:
    case 200:
      return "Ok"
    
    case 404:
      return "Page not found"
    
    case 500:
      return "Internal server error"
    
    case _:
      return "Unknown error"
    

print(https_status(200))
print(https_status(404))
print(https_status(500))
print(https_status(750))