from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse

from db import db

import logging
import pdfkit
import datetime

from bs4 import BeautifulSoup

logging.basicConfig(filename="logs.log", level=logging.INFO, format="[%(asctime)s - %(levelname)s - %(message)s]\t")

app = FastAPI(
    title="API",
    description="API for the project",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Root route. Returns a message explaining how to use the API.
    """
    logging.info("Root route accessed")
    return JSONResponse({"message": "Welcome to the API. All is working fine."}, status_code=200)


@app.get("/company/all")
async def get_companies():
    """
    Get all companies.
    Example cURL command:
        curl -X GET "http://localhost:8000/company/all" -H "accept: application/json"
    Example Python requests code:
        requests.get("http://localhost:8000/company/all")
    """
    logging.info("Get all companies accessed.")
    try:
        companies = db.get_all_companies()
    except Exception as e:
        logging.error(f"Error getting all companies: {e}.")
        return JSONResponse({"message": "Error getting all companies."}, status_code=500)
    return companies


@app.get("/company/get/{cnpj}")
async def get_company(cnpj: str):
    """
    Get a company by its CNPJ.
    Example cURL command:
        curl -X GET "http://localhost:8000/company/get/12345678901234" -H "accept: application/json"
    Example Python requests code:
        requests.get("http://localhost:8000/company/get/12345678901234")
    """
    logging.info(f"Get company by CNPJ {cnpj} accessed.")
    try:
        company = db.get_company_by_cnpj(cnpj)
    except Exception as e:
        logging.error(f"Error getting company by CNPJ {cnpj}: {e}.")
        return JSONResponse({"message": "Error getting company by CNPJ."}, status_code=500)
    return company


@app.get("/company/get/{cnpj}/sectors")
async def get_company_sectors(cnpj: str):
    """
    Get a company's sectors by its CNPJ.
    Example cURL command:
        curl -X GET "http://localhost:8000/company/get/12345678901234/sectors" -H "accept: application/json"
    Example Python requests code:
        requests.get("http://localhost:8000/company/get/12345678901234/sectors")
    """
    logging.info(f"Get company sectors by CNPJ {cnpj} accessed.")
    try:
        company_sectors = db.get_company_sectors_by_cnpj(cnpj)
    except Exception as e:
        logging.error(f"Error getting company sectors by CNPJ {cnpj}: {e}.")
        return JSONResponse({"message": "Error getting company sectors by CNPJ."}, status_code=500)
    return company_sectors


@app.get("/company/all/sectors")
async def get_companies_sectors():
    """
    Get all companies' sectors.
    Example cURL command:
        curl -X GET "http://localhost:8000/company/all/sectors" -H "accept: application/json"
    Example Python requests code:
        requests.get("http://localhost:8000/company/all/sectors")
    """
    logging.info("Get all companies' sectors accessed.")
    try:
        company_sectors = db.get_all_companies_sectors()
    except Exception as e:
        logging.error(f"Error getting all companies' sectors: {e}.")
        return JSONResponse({"message": "Error getting all companies' sectors."}, status_code=500)
    return company_sectors


@app.get("/company/all/report")
async def get_companies_report():
    """
    Get a report of all companies.
    Example cURL command:
        curl -X GET "http://localhost:8000/company/all/report" -H "accept: application/json"
    Example Python requests code:
        requests.get("http://localhost:8000/company/all/report")
    """
    logging.info("Get all companies report accessed.")

    try:
        reports = []
        company_sectors = []

        relatorio_completo = """
        <!DOCTYPE html>
        <html lang="pt">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Empresas</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    padding: 20px;
                    background-color: #f4f4f4;
                }
                h1, h2, h3, h4 {
                    color: #333;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
                .empresa {
                    border-bottom: 2px solid #ddd;
                    padding-bottom: 15px;
                    margin-bottom: 15px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 10px;
                }
                table, th, td {
                    border: 1px solid #ddd;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #007bff;
                    color: white;
                }
                .footer {
                    text-align: center;
                    margin-top: 20px;
                    font-size: 12px;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Relatório de Empresas</h1>
        """

        companies = db.get_all_companies()
        relatorio_completo += f"<p><strong>Total de empresas:</strong> {len(companies)}</p>"
        relatorio_completo += "<h2>Relatório por Empresa:</h2>"

        for company in companies:
            relatorio_completo += f"""
            <div class="empresa">
                <h3>Empresa: {company.nome}</h3>
                <p><strong>CNPJ:</strong> {company.cnpj}</p>
                <p><strong>Endereço:</strong> {company.endereco}</p>
                <p><strong>Setor de Atividade:</strong> {company.setor_atividade}</p>
                <h4>Relatório por Setor:</h4>
                <table>
                    <tr>
                        <th>Setor</th>
                        <th>Total Funcionários</th>
                        <th>Homens</th>
                        <th>Mulheres</th>
                        <th>Taxa Homens</th>
                        <th>Taxa Mulheres</th>
                        <th>Idade Média Homens</th>
                        <th>Idade Média Mulheres</th>
                    </tr>
            """

            company_sectors = db.get_company_sectors_by_cnpj(company.cnpj)
            relatorios = [sector.relatorio() for sector in company_sectors]

            for relatorio in relatorios:
                relatorio_completo += f"""
                    <tr>
                        <td>{relatorio['setor']}</td>
                        <td>{relatorio['total_funcionarios']}</td>
                        <td>{relatorio['qtd_homens']}</td>
                        <td>{relatorio['qtd_mulheres']}</td>
                        <td>{relatorio['taxa_homens']:0.2f}</td>
                        <td>{relatorio['taxa_mulheres']:0.2f}</td>
                        <td>{relatorio['idade_media_homens']:0.2f}</td>
                        <td>{relatorio['idade_media_mulheres']:0.2f}</td>
                    </tr>
                """

            relatorio_completo += "</table></div>"

        relatorio_completo += f"""
            <div class="footer">
                <p>Relatório gerado automaticamente - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
            </div>
            </div>
        </body>
        </html>
        """

        # Beautify HTML
        html = BeautifulSoup(relatorio_completo, 'html.parser')
        relatorio_completo = html.prettify()

        document_bytes = pdfkit.from_string(relatorio_completo, False)

        reports.append({
            'company': f"{company}",
            'document_bytes': document_bytes
        })
    except Exception as e:
        logging.error(f"Error getting all companies report: {e}.")
        return JSONResponse({"message": "Error getting all companies report."}, status_code=500)
    return StreamingResponse(iter([document_bytes]), media_type="application/pdf")


@app.get("/company/get/{cnpj}/report")
async def get_company_report(cnpj: str):
    """
    Get a report of a company by its CNPJ.
    Example cURL command:
        curl -X GET "http://localhost:8000/company/get/12345678901234/report" -H "accept: application/json"
    Example Python requests code:
        requests.get("http://localhost:8000/company/get/12345678901234/report")
    """
    logging.info(f"Get company report by CNPJ {cnpj} accessed.")

    try:
        reports = []
        company = db.get_company_by_cnpj(cnpj)
        company_sectors = db.get_company_sectors_by_cnpj(company.cnpj)
        relatorios = [sector.relatorio() for sector in company_sectors]
        
        relatorio_completo = """
        <!DOCTYPE html>
        <html lang="pt">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Empresas</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    padding: 20px;
                    background-color: #f4f4f4;
                }
                h1, h2, h3, h4 {
                    color: #333;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
                .empresa {
                    border-bottom: 2px solid #ddd;
                    padding-bottom: 15px;
                    margin-bottom: 15px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 10px;
                }
                table, th, td {
                    border: 1px solid #ddd;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #007bff;
                    color: white;
                }
                .footer {
                    text-align: center;
                    margin-top: 20px;
                    font-size: 12px;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Relatório de Empresas</h1>
        """

        relatorio_completo += f"""
            <div class="empresa">
                <h3>Empresa: {company.nome}</h3>
                <p><strong>CNPJ:</strong> {company.cnpj}</p>
                <p><strong>Endereço:</strong> {company.endereco}</p>
                <p><strong>Setor de Atividade:</strong> {company.setor_atividade}</p>
                <h4>Relatório por Setor:</h4>
                <table>
                    <tr>
                        <th>Setor</th>
                        <th>Total Funcionários</th>
                        <th>Homens</th>
                        <th>Mulheres</th>
                        <th>Taxa Homens</th>
                        <th>Taxa Mulheres</th>
                        <th>Idade Média Homens</th>
                        <th>Idade Média Mulheres</th>
            """

        for relatorio in relatorios:
            relatorio_completo += f"""
                <tr>
                    <td>{relatorio['setor']}</td>
                    <td>{relatorio['total_funcionarios']}</td>
                    <td>{relatorio['qtd_homens']}</td>
                    <td>{relatorio['qtd_mulheres']}</td>
                    <td>{relatorio['taxa_homens']:0.2f}</td>
                    <td>{relatorio['taxa_mulheres']:0.2f}</td>
                    <td>{relatorio['idade_media_homens']:0.2f}</td>
                    <td>{relatorio['idade_media_mulheres']:0.2f}</td>
                </tr>
            """

        relatorio_completo += f"""
                </table>
            </div>
            <div class="footer">
                <p>Relatório gerado automaticamente - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
            </div>
            </div>
        </body>
        </html>
        """

        html = BeautifulSoup(relatorio_completo, 'html.parser')
        relatorio_completo = html.prettify()

        document_bytes = pdfkit.from_string(relatorio_completo, False)

        reports.append({
            'company': f"{company}",
            'document_bytes': document_bytes
        })
    except Exception as e:
        logging.error(f"Error getting company report by CNPJ {cnpj}: {e}.")
        return JSONResponse({"message": "Error getting company report by CNPJ."}, status_code=500)
    return StreamingResponse(iter([document_bytes]), media_type="application/pdf")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
