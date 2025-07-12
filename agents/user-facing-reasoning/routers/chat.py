import asyncio
import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from ..services.llm import get_simple_response

router = APIRouter()


@router.get("/chat/stream")
def stream_llm_response():
    async def foo():
        text = """
        Okay, the user is asking about disk allocation algorithms and their trade-offs. Let me start by looking at the provided context. The context mentions different allocation methods like contiguous, linked list, indexed, and specific cases like Windows and Unix-based systems. 
First, contiguous allocation assigns blocks consecutively. That should be fast for access but might lead to fragmentation, right? Then linked lists use pointers, which avoids fragmentation but could have overhead from storing pointers and slower access since you have to traverse the list. 
Indexed allocation, especially with Unix's inodes, uses a multilevel approach. Direct blocks for small files and indirect blocks for larger ones. That offers flexibility but with added complexity. Oh, and Windows uses a file-table linked list, which is like a hybrid maybe?
Wait, the user mentioned disk allocation algorithms, but some of the context refers to disk scheduling algorithms like FCFS, SSTF, SCAN, etc. But the question is about allocation, not scheduling. So I should focus on the file system allocation methods, not the disk head scheduling.
So the main ones are contiguous, linked list, and indexed. Each has trade-offs: contiguous has speed vs. fragmentation; linked has no external fragmentation but sequential access overhead; indexed allows random access but has index block overhead.
Additionally, Unix's inode example allows efficient handling of both small and large files, which is an advantage. Windows' file-table allocation (FAT?) uses a linked list structure but keeps part of it in the file table for faster access. Trade-offs here would be between speed and storage efficiency.
Hmm, the context does not mention other methods like extents or newer techniques, so I should stick to what's provided. Also need to be careful to not confuse disk scheduling with allocation. The answer should clearly outline the three main allocation methods, their working, and their pros and cons as per the context without introducing outside knowledge.
        """
        for word in text.split(" "):
            chunk = {
               "type": "reasoning", "data": f"{word} " 
            }
            yield f"{json.dumps(chunk)}\n\n"
            # yield f"type: reasoning\ndata: {word}\n\n" 
            await asyncio.sleep(.06)

    # return {"type": "reasoning", "data": "Hello world"}
    return StreamingResponse(foo(), media_type="text/event-stream")


@router.get("/chat/simple")
def simple_llm_response():
    answer = get_simple_response("Who are you")
    return {
        "content": f"{answer}",
        "reasoning": "The user asked a simple question about disk allocation algorithms",
    }
