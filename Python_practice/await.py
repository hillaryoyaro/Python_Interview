import asyncio

async def main(name:str) -> str:
   print (name)
   task = asyncio.create_task(foo("Oyaro"))
   await  asyncio.sleep(2)
   await task
   print("Obara")

async def foo(last_name:str) -> str:
    print(last_name)
    await asyncio.sleep(1)  
#asyncio.run(foo("text"))     
asyncio.run(main("Hillary"))

