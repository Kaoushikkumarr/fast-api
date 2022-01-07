"""
All Paths(i.e, also called as End-Points) are defined here.
"""
import json
import requests
from model import models
from controller import crud
from fastapi import Depends
from connect import cnf_dict
from sqlalchemy.orm import Session
from schema_mapping import schemas
from authentication.ouath2 import get_current_user
from fastapi import APIRouter, HTTPException, status
from infrastructure.database import get_db_connection, session


engine = get_db_connection().engine  # created object/instance

router = APIRouter(
    prefix='/do-select',
    tags=['Do-Select']
)

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    try:
        yield session
    finally:
        session.close()


@router.get('/')
def read():
    do_select_url = cnf_dict['DO_SELECT']['do_select_url']
    header = {
        'DoSelect-Api-Key': cnf_dict['DO_SELECT']['do_select_api_key'],
        'DoSelect-Api-Secret': cnf_dict['DO_SELECT']['do_select_api_secret']
    }
    data = requests.get(url=do_select_url, headers=header)
    if not data:
        return {'response': 'No Data Found'}
    return data.json()


@router.post("/assessment", response_model=schemas.Assessment)
def create_assessment(
        assessment: schemas.AssessmentCreate,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_assessment(assessment, db=db)


@router.get("/assessment/{slug_id}", response_model=schemas.Assessment)
def read_slug(
        slug_id: int,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(models.Assessment).filter(models.Assessment.id == slug_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Slug Id Not Found')
    return data


@router.post("/tenant", response_model=schemas.Tenant)
def create_tenant(
        tenant: schemas.Tenant,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_tenant(tenant, db)


@router.get("/tenant/{tenant_name}", response_model=schemas.Tenant)
def read_tenant(
        tenant_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(models.Tenant).filter(models.Tenant.tenant_name == tenant_name).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tenant Not Found')
    return data


@router.post("/skill_master", response_model=schemas.SkillMaster)
def create_skill(
        skill: schemas.SkillMaster,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_skill(skill, db)


@router.get("/skill_master/{skill_name}", response_model=schemas.SkillMaster)
def read_skill(
        skill_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(models.SkillMaster).filter(models.SkillMaster.skill_name == skill_name).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Skill Not Found')
    return data


@router.post("/partner_type", response_model=schemas.Partner)
def create_partner(
        partner: schemas.Partner,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_partner(partner, db)


@router.get("/partner_type/{partner_name}", response_model=schemas.Partner)
def read_partner(
        partner_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(models.PartnerType).filter(models.PartnerType.partner_name == partner_name).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Skill Not Found')
    return data


@router.post("/application", response_model=schemas.Application)
def create_application(
        application: schemas.Application,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_application(application, db)


@router.get("/application/{application_name}", response_model=schemas.Application)
def read_application(
        application_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.ApplicationMaster).filter(
        models.ApplicationMaster.application_name == application_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Skill Not Found')
    return data


@router.put("/application/{application_name}", response_model=schemas.Application)
def update_application(
        application_name: str,
        application: schemas.Application,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.update_application(application_name, application, db)


@router.delete("/application/{application_name}", response_model=schemas.Application)
def delete_application(
        application_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.ApplicationMaster).filter(
        models.ApplicationMaster.application_name == application_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Application Name Not Found!')
    return crud.delete_application(application_name,  db)


@router.post("/category", response_model=schemas.CategoryMaster)
def create_category(
        category: schemas.CategoryMaster,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_category(category, db)


@router.get("/category/{category_type}", response_model=schemas.CategoryMaster)
def read_category(
        category_type: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.CategoryMaster).filter(
        models.CategoryMaster.category_type == category_type
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Type Not Found!')
    return data


@router.put("/category/{category_type}", response_model=schemas.CategoryMaster)
def update_category(
        category_type: str,
        category: schemas.CategoryMaster,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.update_category(category_type, category, db)


@router.delete("/category/{category_type}", response_model=schemas.CategoryMaster)
def delete_category(
        category_type: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.CategoryMaster).filter(
        models.CategoryMaster.category_type == category_type
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Type Not Found!')
    return crud.delete_category(category_type,  db)


@router.post("/assessment_partner", response_model=schemas.AssessmentPartner)
def create_assessment_partner(
        assessment_partner: schemas.AssessmentPartner,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_assessment_partner(assessment_partner, db)


@router.get("/assessment_partner/{partner_name}", response_model=schemas.AssessmentPartner)
def read_assessment_partner(
        partner_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.AssessmentPartner).filter(
        models.AssessmentPartner.partner_name == partner_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Type Not Found!')
    return data


@router.put("/assessment_partner/{partner_name}", response_model=schemas.AssessmentPartner)
def update_assessment_partner(
        partner_name: str,
        partner: schemas.AssessmentPartner,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.update_assessment_partner(partner_name, partner, db)


@router.delete("/assessment_partner/{partner_name}", response_model=schemas.AssessmentPartner)
def delete_assessment_partner(
        partner_name: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.AssessmentPartner).filter(
        models.AssessmentPartner.partner_name == partner_name
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Type Not Found!')
    return crud.delete_assessment_partner(partner_name,  db)


@router.post("/subscription", response_model=schemas.SubscriptionMaster)
def create_subscription(
        subscription: schemas.SubscriptionMaster,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_subscription(subscription, db)


@router.get("/subscription/{subscription_id}", response_model=schemas.SubscriptionMaster)
def read_assessment_partner(
        subscription_id: int,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.SubscriptionMaster).filter(
        models.SubscriptionMaster.id == subscription_id
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Subscription ID Not Found!')
    return data


@router.post("/assessment_mapping", response_model=schemas.AssessmentMapping)
def create_mapping(
        mapping: schemas.AssessmentMapping,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    return crud.create_mapping(mapping, db)


@router.get("/assessment_mapping", response_model=schemas.AssessmentMapping)
def read_assessment_partner(
        mapping_id: int,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.
    data = db.query(
        models.AssessmentMapping).filter(
        models.AssessmentMapping.id == mapping_id
    ).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Assessment Mapping Not Found!')
    return data


@router.get("/assessment_integration/{client_name}/{application_name}/{skill_name}/{category_type}")
def read_assessment_integration(
        client_name: str,
        application_name: str,
        skill_name: str,
        category_type: str,
        db: Session = Depends(get_db),
        current_user: schemas.SignUp = Depends(get_current_user)):  # This is line will allow user to use credentials.

    client = db.query(models.Tenant).filter(models.Tenant.tenant_name == client_name).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Client Not Found!')

    if client.status:
        subscription = db.query(models.SubscriptionMaster).filter(
            models.SubscriptionMaster.tenant_id == client.id,
            models.SubscriptionMaster.subscription is True
        )
        if not subscription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Subscription Not Found for this Client!')

    application = db.query(
        models.ApplicationMaster).filter(models.ApplicationMaster.application_name == application_name).first()
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Assessment Not Mapped')
    application_id = application.id

    skill = db.query(models.SkillMaster).filter(models.SkillMaster.skill_name == skill_name).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Skill Not Found!')

    category = db.query(models.CategoryMaster).filter(models.CategoryMaster.category_type == category_type).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Not Found!')

    application_mapping = db.query(models.AssessmentMapping). \
        filter(models.AssessmentMapping.skill_master_id == skill.id,
               models.AssessmentMapping.assessment_partner_id == client.id,
               models.AssessmentMapping.category_master_id == category.id).all()

    if not application_mapping:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Skill Not Found!')
    final_dict = {}
    result = []
    for app_details in application_mapping:
        partner_subscription = db.query(models.AssessmentPartner). \
            filter(models.AssessmentPartner.id == app_details.assessment_partner_id).first()
        if not partner_subscription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Assessment Partner Not Found!')

        assessment_partner_name = partner_subscription.partner_name
        test_url = app_details.test_url
        test_slug = app_details.test_id

        do_select_api_key = cnf_dict['DO_SELECT']['do_select_api_key']
        do_select_api_secret = cnf_dict['DO_SELECT']['do_select_api_secret']
        do_select_url = cnf_dict['DO_SELECT']['do_select_url'] + '/' + test_slug
        header = {
            'DoSelect-Api-Key': do_select_api_key,
            'DoSelect-Api-Secret': do_select_api_secret
        }
        response = requests.get(do_select_url, headers=header)
        result.append(json.loads(response.text))

        final_dict['total_candidates'] = result[0].get('total_candidates', 0)
        final_dict['duration'] = result[0].get('duration', 0)
        final_dict['public_access_url'] = result[0].get('public_access_url', 0)
        final_dict['test_url'] = test_url
        final_dict['test_slug'] = test_slug
        final_dict['assessment_partner_name'] = assessment_partner_name
    return final_dict


