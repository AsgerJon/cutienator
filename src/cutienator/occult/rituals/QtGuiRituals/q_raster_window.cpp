//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qrasterwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qrasterwindow.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QRasterWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QRasterWindow10metaObjectEv(
    const QRasterWindow *self) {
  return self->metaObject();
}

//  QString QRasterWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QRasterWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRasterWindow::tr(s, c, n));
}

//  QRasterWindow::QRasterWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QRasterWindow *ritual_ZN13QRasterWindowC1EP7QWindow(QWindow *parent) {
  return new QRasterWindow(parent);
}

//  QRasterWindow::~QRasterWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRasterWindowD1Ev(QRasterWindow *self) {
  delete self;
}
