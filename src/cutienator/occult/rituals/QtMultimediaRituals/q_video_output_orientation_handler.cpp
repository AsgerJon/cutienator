//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qvideooutputorientationhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideooutputorientationhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QVideoOutputOrientationHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QVideoOutputOrientationHandler10metaObjectEv(
    const QVideoOutputOrientationHandler *self) {
  return self->metaObject();
}

//  void *QVideoOutputOrientationHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QVideoOutputOrientationHandler11qt_metacastEPKc(
    QVideoOutputOrientationHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVideoOutputOrientationHandler::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QVideoOutputOrientationHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QVideoOutputOrientationHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVideoOutputOrientationHandler::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QVideoOutputOrientationHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVideoOutputOrientationHandler::tr(s, c, n));
}

//  QVideoOutputOrientationHandler::QVideoOutputOrientationHandler(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QVideoOutputOrientationHandler *ritual_ZN30QVideoOutputOrientationHandlerC1EP7QObject(
    QObject *parent) {
  return new QVideoOutputOrientationHandler(parent);
}

//  int QVideoOutputOrientationHandler::currentOrientation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QVideoOutputOrientationHandler18currentOrientationEv(
    const QVideoOutputOrientationHandler *self) {
  return self->currentOrientation();
}

//  void QVideoOutputOrientationHandler::setIsRecording(bool isRecording)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QVideoOutputOrientationHandler14setIsRecordingEb(
    bool isRecording) {
  QVideoOutputOrientationHandler::setIsRecording(isRecording);
}

//  bool QVideoOutputOrientationHandler::isRecording()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QVideoOutputOrientationHandler11isRecordingEv() {
  return QVideoOutputOrientationHandler::isRecording();
}

//  void QVideoOutputOrientationHandler::orientationChanged(int angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QVideoOutputOrientationHandler18orientationChangedEi(
    QVideoOutputOrientationHandler *self,
    int angle) {
  self->orientationChanged(angle);
}

//  void QVideoOutputOrientationHandler::screenOrientationChanged(Qt::ScreenO
//      rientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QVideoOutputOrientationHandler24screenOrientationChangedEN2Qt17ScreenOrientationE(
    QVideoOutputOrientationHandler *self,
    Qt::ScreenOrientation orientation) {
  self->screenOrientationChanged(orientation);
}
