//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(egl)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QOpenGLCompositor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QOpenGLCompositor10metaObjectEv(
    const QOpenGLCompositor *self) {
  return self->metaObject();
}

//  void *QOpenGLCompositor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QOpenGLCompositor11qt_metacastEPKc(
    QOpenGLCompositor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLCompositor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QOpenGLCompositor11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLCompositor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLCompositor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QOpenGLCompositor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLCompositor::tr(s, c, n));
}

//  QOpenGLCompositor *QOpenGLCompositor::instance()
extern "C" Q_DECL_EXPORT
QOpenGLCompositor *ritual_ZN17QOpenGLCompositor8instanceEv() {
  return QOpenGLCompositor::instance();
}

//  void QOpenGLCompositor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor7destroyEv() {
  QOpenGLCompositor::destroy();
}

//  void QOpenGLCompositor::setTargetWindow(QWindow *window, const QRect
//      &nativeTargetGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor15setTargetWindowEP7QWindowRK5QRect(
    QOpenGLCompositor *self,
    QWindow *window,
    const QRect *nativeTargetGeometry) {
  self->setTargetWindow(window, *nativeTargetGeometry);
}

//  void QOpenGLCompositor::setTargetContext(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor16setTargetContextEP14QOpenGLContext(
    QOpenGLCompositor *self,
    QOpenGLContext *context) {
  self->setTargetContext(context);
}

//  void QOpenGLCompositor::setRotation(int degrees)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor11setRotationEi(
    QOpenGLCompositor *self,
    int degrees) {
  self->setRotation(degrees);
}

//  QOpenGLContext *QOpenGLCompositor::context() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK17QOpenGLCompositor7contextEv(
    const QOpenGLCompositor *self) {
  return self->context();
}

//  QWindow *QOpenGLCompositor::targetWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK17QOpenGLCompositor12targetWindowEv(
    const QOpenGLCompositor *self) {
  return self->targetWindow();
}

//  QRect QOpenGLCompositor::nativeTargetGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QOpenGLCompositor20nativeTargetGeometryEv(
    const QOpenGLCompositor *self) {
  return new QRect(self->nativeTargetGeometry());
}

//  void QOpenGLCompositor::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor6updateEv(QOpenGLCompositor *self) {
  self->update();
}

//  QImage QOpenGLCompositor::grab()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN17QOpenGLCompositor4grabEv(QOpenGLCompositor *self) {
  return new QImage(self->grab());
}

//  bool QOpenGLCompositor::grabToFrameBufferObject(QOpenGLFramebufferObject
//      *fbo, GrabOrientation orientation)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QOpenGLCompositor23grabToFrameBufferObjectEP24QOpenGLFramebufferObjectNS_15GrabOrientationE(
    QOpenGLCompositor *self,
    QOpenGLFramebufferObject *fbo,
    QOpenGLCompositor::GrabOrientation orientation) {
  return self->grabToFrameBufferObject(fbo, orientation);
}

//  QList<QOpenGLCompositorWindow *> QOpenGLCompositor::windows() const
extern "C" Q_DECL_EXPORT
QList<QOpenGLCompositorWindow *> *ritual_ZNK17QOpenGLCompositor7windowsEv(
    const QOpenGLCompositor *self) {
  return new QList<QOpenGLCompositorWindow *>(self->windows());
}

//  void QOpenGLCompositor::addWindow(QOpenGLCompositorWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor9addWindowEP23QOpenGLCompositorWindow(
    QOpenGLCompositor *self,
    QOpenGLCompositorWindow *window) {
  self->addWindow(window);
}

//  void QOpenGLCompositor::removeWindow(QOpenGLCompositorWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor12removeWindowEP23QOpenGLCompositorWindow(
    QOpenGLCompositor *self,
    QOpenGLCompositorWindow *window) {
  self->removeWindow(window);
}

//  void QOpenGLCompositor::moveToTop(QOpenGLCompositorWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor9moveToTopEP23QOpenGLCompositorWindow(
    QOpenGLCompositor *self,
    QOpenGLCompositorWindow *window) {
  self->moveToTop(window);
}

//  void QOpenGLCompositor::changeWindowIndex(QOpenGLCompositorWindow
//      *window, int newIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor17changeWindowIndexEP23QOpenGLCompositorWindowi(
    QOpenGLCompositor *self,
    QOpenGLCompositorWindow *window,
    int newIdx) {
  self->changeWindowIndex(window, newIdx);
}

//  void QOpenGLCompositor::topWindowChanged(QOpenGLCompositorWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor16topWindowChangedEP23QOpenGLCompositorWindow(
    QOpenGLCompositor *self,
    QOpenGLCompositorWindow *window) {
  self->topWindowChanged(window);
}

//  void QOpenGLCompositor::handleRenderAllRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor22handleRenderAllRequestEv(
    QOpenGLCompositor *self) {
  self->handleRenderAllRequest();
}

//  QOpenGLCompositor::QOpenGLCompositor()
extern "C" Q_DECL_EXPORT
QOpenGLCompositor *ritual_ZN17QOpenGLCompositorC1Ev() {
  return new QOpenGLCompositor();
}

//  QOpenGLCompositor::~QOpenGLCompositor()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositorD1Ev(QOpenGLCompositor *self) {
  delete self;
}

//  void QOpenGLCompositor::renderAll(QOpenGLFramebufferObject *fbo,
//      QOpenGLTextureBlitter::Origin origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor9renderAllEP24QOpenGLFramebufferObjectN21QOpenGLTextureBlitter6OriginE(
    QOpenGLCompositor *self,
    QOpenGLFramebufferObject *fbo,
    QOpenGLTextureBlitter::Origin origin) {
  self->renderAll(fbo, origin);
}

//  void QOpenGLCompositor::render(QOpenGLCompositorWindow *window,
//      QOpenGLTextureBlitter::Origin origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor6renderEP23QOpenGLCompositorWindowN21QOpenGLTextureBlitter6OriginE(
    QOpenGLCompositor *self,
    QOpenGLCompositorWindow *window,
    QOpenGLTextureBlitter::Origin origin) {
  self->render(window, origin);
}

//  void QOpenGLCompositor::ensureCorrectZOrder()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLCompositor19ensureCorrectZOrderEv(
    QOpenGLCompositor *self) {
  self->ensureCorrectZOrder();
}

#endif  // QT_CONFIG(egl)
