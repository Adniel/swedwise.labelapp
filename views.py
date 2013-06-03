from pyramid.view import view_config
from pyramid.response import FileResponse
from godsflagga import Godsflagga
import os

@view_config(renderer="index.pt")
def index_view(request):
    return {}


@view_config(name='render')
def test_page(request):
    g = Godsflagga(request.POST['part_no'], request.POST['quantity'],
                   request.POST['vendor_lot'], request.POST['vendor_number'],
                   request.POST['serial'],request.POST['description'],
                   request.POST['date'],request.POST['po_number'])

    filedict = g.create()

    response = FileResponse(
        filedict.get('FILENAMEPATH'),
        request=request,
        content_type='application/pdf',
        )
    response.content_disposition = 'attachment; filename="%s"' % filedict.get('FILENAME')
    try:
        os.remove(filedict.get('FILENAMEPATH'))
    except Exception, ex:
        print 'Could not remove file', ex

    return response