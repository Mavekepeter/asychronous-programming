import asyncio
async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(10)  #stimulating an input/out device
    print("Done fetching")
    return{'data':1}

async def print_numbers():
    for i in range(20):
        print (i)
        await asyncio.sleep(1)
        
async def main():
    task1=asyncio.create_task(fetch_data())
    task2=asyncio.create_task(print_numbers())
    value=await task1
    print(value)
    
asyncio.run(main())
        