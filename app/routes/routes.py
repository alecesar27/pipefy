from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services import api_pipefy


router = APIRouter()


@router.post("/create-pipe/")
async def create_pipe(organization_id: int,name: str ):
    try:
        result = api_pipefy.create_pipe(organization_id,name)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/update-pipe/{pipe_id}")
async def update_pipe(pipe_id: int, name: str):
    try:
        result = api_pipefy.update_pipe(pipe_id, name)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/pipe/reports/{pipe_id}")
async def get_reports(pipe_id: int):
    try:
        result = api_pipefy.get_pipe_reports(pipe_id)
        return result.get("data", {}).get("pipe", {}).get("reports", [])
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/export-pipe-report")
async def export_pipe_report(pipe_id: int, pipe_report_id: int):
    try:
        result = api_pipefy.export_pipe_report(pipe_id, pipe_report_id)
        return result.get("data", {}).get("exportPipeReport", {}).get("pipeReportExport", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

@router.get("/list-pipes/")
async def list_pipes():
    try:
        result = api_pipefy.list_pipes()
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/organization/")
async def get_organization():
    try:
        result = api_pipefy.get_organization()
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

@router.delete("/delete-pipe/{pipe_id}")
async def delete_pipe(pipe_id: int):
    try:
        result = api_pipefy.delete_pipe(pipe_id)
        if result.get("data", {}).get("deletePipe", {}).get("success"):
            return {"message": "Pipe deleted successfully"}
        else:
            raise HTTPException(status_code=400, detail="Failed to delete pipe")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-phase")
async def create_phase(pipe_id: str, name: str):
    try:
        result = api_pipefy.create_phase(pipe_id, name)
        return result.get("data", {}).get("createPhase", {}).get("phase", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update-phase")
async def update_phase(phase_id: int, color: str, name: str):
    try:
        result = api_pipefy.update_phase(phase_id, color, name)
        return result.get("data", {}).get("updatePhase", {}).get("phase", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete-phase")
async def delete_phase(phase_id: int):
    try:
        result = api_pipefy.delete_phase(phase_id)
        return result.get("data", {}).get("deletePhase", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/phase/{phase_id}")
async def get_phase(phase_id: int):
    try:
        result = api_pipefy.get_phase(phase_id)
        return result.get("data", {}).get("phase", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-phase-field")
async def create_phase_field(phase_id: int, label: str, field_type: str, options: list):
    try:
        result = api_pipefy.create_phase_field(phase_id, label, field_type, options)
        return result.get("data", {}).get("createPhaseField", {}).get("phase_field", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.put("/update-phase-field")
async def update_phase_field(field_id: str, label: str, required: bool):
    try:
        result = api_pipefy.update_phase_field(field_id, label, required)
        return result.get("data", {}).get("updatePhaseField", {}).get("phase_field", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete-phase-field")
async def delete_phase_field(pipe_uuid: str, field_id: str):
    try:
        result = delete_phase_field(pipe_uuid, field_id)
        return result.get("data", {}).get("deletePhaseField", {})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cards/{pipe_id}")
async def read_cards(pipe_id: int):
    try:
        cards = api_pipefy.get_all_cards(pipe_id)
        return cards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/all-card-details/{pipe_id}")
async def read_all_card_details(pipe_id: int):
    try:
        cards = api_pipefy.get_all_card_details(pipe_id)
        return cards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/card-details/{pipe_id}/{id_card}")
async def read_card_details(pipe_id: int, id_card: str):
    try:
        card = api_pipefy.get_card_details(pipe_id, id_card)
        return card
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/create-card/")
async def create_card(pipe_id: str, title: str):
    try:
        result = api_pipefy.create_card(pipe_id, title)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/update-card-title/{card_id}")
async def update_card_title(card_id: str, title: str = None):
    try:
        result = api_pipefy.update_title_card(card_id, title)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/delete-card/{card_id}")
async def delete_card(card_id: str):
    try:
        result = api_pipefy.delete_card(card_id)
        if result.get("data", {}).get("deleteCard", {}).get("success"):
            return {"message": "Card deleted successfully"}
        else:
            raise HTTPException(status_code=400, detail="Failed to delete card")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

#print(create_pipe('Melhor Pipe do Mundo',301424863))
#print(update_pipe(305487792, 'Melhor Pipe do Mundo Dobrado'))
#print(delete_pipe(305487792))
#print(get_all_cards(305087031))
#ids=['305087790']
#print(list_pipes(url,ids))
#print(get_all_card_details(305087031))
#print(get_card_details(305087031,'1025275646'))
#print(list_pipes())

# pipe_id = 305087031  # Substitua pelo ID do seu pipe
# novo_card = create_card(pipe_id, 'Criar Tela de Login')
# print("Novo Card:", novo_card)
#id_card='1029774496'
# updated_card = update_title_card(id_card,'Criar a Tela de Login X')
# print(updated_card)
#print(delete_card(id_card))


# print(api_pipefy.get_all_cards(305087031))

