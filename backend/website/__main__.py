import uvicorn
import website
port = 8001

app = website.Application()

uvicorn.run(app, host='0.0.0.0', port=port)
