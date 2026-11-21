//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qimageiohandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QImageIOPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QImageIOPlugin10metaObjectEv(
    const QImageIOPlugin *self) {
  return self->metaObject();
}

//  QString QImageIOPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QImageIOPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QImageIOPlugin::tr(s, c, n));
}

//  QImageIOPlugin::~QImageIOPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QImageIOPluginD1Ev(QImageIOPlugin *self) {
  delete self;
}

//  Capabilities QImageIOPlugin::capabilities(QIODevice *device, const
//      QByteArray &format) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QImageIOPlugin12capabilitiesEP9QIODeviceRK10QByteArray(
    const QImageIOPlugin *self,
    QIODevice *device,
    const QByteArray *format) {
  return static_cast<int>(self->capabilities(device, *format).toInt());
}

//  QImageIOHandler *QImageIOPlugin::create(QIODevice *device, const
//      QByteArray &format) const
extern "C" Q_DECL_EXPORT
QImageIOHandler *ritual_ZNK14QImageIOPlugin6createEP9QIODeviceRK10QByteArray(
    const QImageIOPlugin *self,
    QIODevice *device,
    const QByteArray *format) {
  return self->create(device, *format);
}
