import os
from aiohttp import web
from datetime import datetime
from xhtml2pdf import pisa

from xhtml2pdf.config.httpconfig import httpConfig

import logging
logger = logging.getLogger(__name__)

# Utility function
async def convertHtmlToPdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")
    httpConfig.save_keys('nosslcheck', True)
    pisaStatus = pisa.CreatePDF(
            sourceHtml,
            dest=resultFile)

    resultFile.close()

    return pisaStatus.err


async def healthCheck(request):
    logger.info("CALLED HEALTH CHECK.")
    print("called health check")
    return web.json_response({"msg": "queue server up and running"}, status=200)

async def generatePDF(request):
    print("generatePDF() Created")

    timestamp = datetime.timestamp(datetime.now())

    # Define your data
    sourceHtml = """
        <html>
        <head>
            <style>
                @page {
                    size: letter portrait;
                    margin: 2cm;
                }
                
                p { margin: 0; }
                .header_date {
                    font-size: 10pt;
                }

                table { -pdf-keep-with-next: true; }
            </style>
        <head>
        <body style="background:#fff;color:#677a89;">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <span style="font-size:10pt;">Date: 21/05/2019</span>
                        </td>
                        <td style="text-align:right;">
                            <img width='200px' src='https://mytonic.com//sites/all/themes/tonicplus/dist/images/tonic-logo.png' alt='Tonic Logo'>
                        </td>
                    </tr>
                    <tr style="padding-top: .5cm;">
                        <td>
                            <span style="font-size:22pt;color:#677a89;">INVOICE</span><br>
                            <span style="font-size:8pt;">ORDER 10000010</span>
                        </td>
                        <td style="text-align:right;">
                            <img width='200px' src='https://s3-production.mytonic.com/revamp/s3fs-public/thyrocare-logo.png' alt='Thyrocare Logo'>
                        </td>
                        <tr style="padding-top: .4cm;">
                            <td colspan="2">
                                <span style='font-size:16pt;color:#404448;'>Thank you for your purchase!</span>
                                <br>
                                <br>
                                <span style='font-size:10pt;margin-top:.3cm;'>Hi, We are getting your order ready to be shipped. We will notify you when it has been sent</span>
                            </td>
                        </tr>
                    </tr>
                </tbody>
            </table>
            
            <br>
            <br>
            <br>
            <hr style="display:block;border-color:#DCDCDC;background-color:#DCDCDC;padding:1cm 0;">
            <br>
            <br>
            <br>
            
            <table>
                <tbody>
                    <tr>
                        <td>
                            <span style='font-size:16pt;color:#404448;'>Order Summary</span><br>
                        </td>
                        <td style="text-align:right;">
                            <span style="font-size:16pt;border:1px solid #00b450;color:#00b450;padding:10px 5px 0px 5px;width:40px;text-align:center;display:inline-block;">PAID</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span style='color:#404448;'>Type - Item</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>Price (tk)</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span style='color:#404448;'>1. Diabetes Test with a Free Diabetes Machine</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>6,199.00</span>
                        </td>
                    </tr>
                </tbody>
            </table>

            <br>
            <br>
            <hr style="display:block;border-color:#DCDCDC;background-color:#DCDCDC;padding:1cm 0;">
            <br>
            <br>

            <table>
                <tbody>
                    <tr>
                        <td>
                            <span style='color:#404448;'>Subtotal</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>6,199.00</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span style='color:#404448;'>Tonic Discount</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>0.00</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span style='color:#404448;'>Total Price</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>6,199.00</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span style='color:#404448;'>Delivery Fee</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>0.00</span>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <hr>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span style='color:#404448;'>Net Payable</span>
                        </td>
                        <td style="text-align:right;">
                            <span style='color:#404448;'>6,199.00</span>
                        </td>
                    </tr>
                </tbody>
            </table>

            <br>
            <br>
            <hr style="display:block;border-color:#DCDCDC;background-color:#DCDCDC;padding:1cm 0;">
            <br>
            <br>

            <table>
                <tbody>
                    <tr>
                        <td colspan="2">
                            <span>Customer Information</span>
                            <br>
                            <span>Abdullah Al Noman</span>
                            <br>
                            <span>Address: House no 3/A, Road 4, Block C, Gulshan, Dhaka 1212
                            Phone: +8801712345678</span>
                            <br>
                        </td>
                    </tr>
                </tbody>
            </table>

            <br>
            <br>
            <hr style="display:block;border-color:#DCDCDC;background-color:#DCDCDC;padding:1cm 0;">
            <br>
            <br>

            <table>
                <tbody>
                    <tr>
                        <td colspan="2">
                            <span>Contact us</span>
                            <br>
                            <span>Hotline: (+88) 09666737373 / (+88) 01944443850 (+88) 01944443851 </span>
                            <br>
                            <span>Address: House no 3/A, Road 4, Block C, Gulshan, Dhaka 1212 Phone: +8801712345678</span>
                            <br>
                            <span>Address: Confidence Centre (12th floor), Kha-9, Pragoti Sarani, Shazadpur, Gulshan, Dhaka -1212, Bangladesh</span>
                        </td>
                    </tr>
                </tbody>
            </table>

        </body>
        </html>
    """
    outputFilename = "INVOICE-{}.pdf".format(timestamp)

    pisa.showLogging()
    generated = await convertHtmlToPdf(sourceHtml, outputFilename)
    print("PDF Created Result: {}".format(generated))
    
    return web.json_response({"msg": "PDF created"}, status=200)


app = web.Application()

app.add_routes([
    web.get('/', healthCheck),
    web.get('/pdf', generatePDF),
])