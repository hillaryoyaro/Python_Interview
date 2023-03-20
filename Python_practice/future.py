import asyncio

async def fetch_data():
    print("start fetching data")
    await asyncio.sleep(2)
    print("Done fetching data")
    return {'data':1}

async def print_number():
  
    for x in range(10):
        print(x)
    await asyncio.sleep(0.25) 

#create our main function of the program
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_number())

    value = await task1
    print(value)

asyncio.run(main())