from django.test import TestCase

# Create your tests here.
from offer_letter.models import offer1
class offertest(TestCase):
    """offer model tests."""

    def test_str(self):

        global offer
        offer = offer(name='raman',)

        self.assertEquals(
            str(offer),
            'raman',
        )


"""

def test_qr(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="letter.pdf"'

    p = canvas.Canvas(response)

    p.drawString(250, 250, "welcome to nescode")
    qrw = QrCodeWidget('hello world')
    b = qrw.getBounds()

    w = b[2] - b[0]
    h = b[3] - b[1]
    d = UpdateView

    d = Drawing(45, 45, transform=[45. / w, 0, 0, 45. / h, 0, 0])


    d.add(qrw)

    renderPDF.draw(d, p, 1, 1)

    p.showPage()
    p.save()
    return response
"""""