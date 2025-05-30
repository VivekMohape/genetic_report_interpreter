from pydantic import BaseModel, Field
from typing import List, Optional

class VariantAnalysis(BaseModel):
    variant_name: str = Field(..., description="Genetic variant identifier, e.g. BRCA1 c.68_69delAG")
    risk_level: str = Field(..., description="Risk category such as 'High', 'Moderate', or 'Low'")
    associated_conditions: List[str] = Field(..., description="Diseases or conditions linked to the variant")
    drug_response: Optional[str] = Field(None, description="Response impact for known drugs if any")
    recommendations: Optional[str] = Field(None, description="Recommended clinical actions or lifestyle changes")

class GeneticReportResponse(BaseModel):
    report_id: str = Field(..., description="Unique identifier for the uploaded report")
    interpretation_date: str = Field(..., description="Date of LLM interpretation")
    variants: List[VariantAnalysis] = Field(..., description="List of analyzed genetic variants")
