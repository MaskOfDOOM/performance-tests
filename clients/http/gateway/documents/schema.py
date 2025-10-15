from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Описание структуры документа
    """
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении документа с описанием тарифа.
    """
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении документа с описанием условий контракта.
    """
    contract: DocumentSchema