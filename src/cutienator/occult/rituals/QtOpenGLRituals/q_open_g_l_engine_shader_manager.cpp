//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpenGLEngineShaderManager that Python can take functions over in. Every QOpenGLEngineShaderManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLEngineShaderManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLEngineShaderManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLEngineShaderManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLEngineShaderManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLEngineShaderManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLEngineShaderManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLEngineShaderManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLEngineShaderManager : public QOpenGLEngineShaderManager {
public:
  using QOpenGLEngineShaderManager::QOpenGLEngineShaderManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall0 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall1 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall2 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall3 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall4 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall5 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLEngineShaderManagerCall6 call = reinterpret_cast<CuteQOpenGLEngineShaderManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLEngineShaderManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QOpenGLEngineShaderManager10metaObjectEv(
    const QOpenGLEngineShaderManager *self) {
  return self->metaObject();
}

//  void *QOpenGLEngineShaderManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QOpenGLEngineShaderManager11qt_metacastEPKc(
    QOpenGLEngineShaderManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLEngineShaderManager::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QOpenGLEngineShaderManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLEngineShaderManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLEngineShaderManager::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QOpenGLEngineShaderManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLEngineShaderManager::tr(s, c, n));
}

//  QOpenGLEngineShaderManager::QOpenGLEngineShaderManager(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
QOpenGLEngineShaderManager *ritual_ZN26QOpenGLEngineShaderManagerC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new CuteQOpenGLEngineShaderManager(context);
}

//  QOpenGLEngineShaderManager::~QOpenGLEngineShaderManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManagerD1Ev(
    QOpenGLEngineShaderManager *self) {
  delete self;
}

//  void QOpenGLEngineShaderManager::optimiseForBrushTransform(QTransform::Tr
//      ansformationType transformType)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager25optimiseForBrushTransformEN10QTransform18TransformationTypeE(
    QOpenGLEngineShaderManager *self,
    QTransform::TransformationType transformType) {
  self->optimiseForBrushTransform(transformType);
}

//  void QOpenGLEngineShaderManager::setSrcPixelType(Qt::BrushStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager15setSrcPixelTypeEN2Qt10BrushStyleE(
    QOpenGLEngineShaderManager *self,
    Qt::BrushStyle a0) {
  self->setSrcPixelType(a0);
}

//  void QOpenGLEngineShaderManager::setSrcPixelType(PixelSrcType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager15setSrcPixelTypeENS_12PixelSrcTypeE(
    QOpenGLEngineShaderManager *self,
    QOpenGLEngineShaderManager::PixelSrcType a0) {
  self->setSrcPixelType(a0);
}

//  void QOpenGLEngineShaderManager::setOpacityMode(OpacityMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager14setOpacityModeENS_11OpacityModeE(
    QOpenGLEngineShaderManager *self,
    QOpenGLEngineShaderManager::OpacityMode a0) {
  self->setOpacityMode(a0);
}

//  void QOpenGLEngineShaderManager::setMaskType(MaskType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager11setMaskTypeENS_8MaskTypeE(
    QOpenGLEngineShaderManager *self,
    QOpenGLEngineShaderManager::MaskType a0) {
  self->setMaskType(a0);
}

//  void
//      QOpenGLEngineShaderManager::setCompositionMode(QPainter::CompositionM
//      ode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager18setCompositionModeEN8QPainter15CompositionModeE(
    QOpenGLEngineShaderManager *self,
    QPainter::CompositionMode a0) {
  self->setCompositionMode(a0);
}

//  void QOpenGLEngineShaderManager::setCustomStage(QOpenGLCustomShaderStage
//      *stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager14setCustomStageEP24QOpenGLCustomShaderStage(
    QOpenGLEngineShaderManager *self,
    QOpenGLCustomShaderStage *stage) {
  self->setCustomStage(stage);
}

//  void QOpenGLEngineShaderManager::removeCustomStage()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager17removeCustomStageEv(
    QOpenGLEngineShaderManager *self) {
  self->removeCustomStage();
}

//  GLuint QOpenGLEngineShaderManager::getUniformLocation(Uniform id)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN26QOpenGLEngineShaderManager18getUniformLocationENS_7UniformE(
    QOpenGLEngineShaderManager *self,
    QOpenGLEngineShaderManager::Uniform id) {
  return self->getUniformLocation(id);
}

//  void QOpenGLEngineShaderManager::setDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager8setDirtyEv(
    QOpenGLEngineShaderManager *self) {
  self->setDirty();
}

//  bool QOpenGLEngineShaderManager::useCorrectShaderProg()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QOpenGLEngineShaderManager20useCorrectShaderProgEv(
    QOpenGLEngineShaderManager *self) {
  return self->useCorrectShaderProg();
}

//  void QOpenGLEngineShaderManager::useSimpleProgram()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager16useSimpleProgramEv(
    QOpenGLEngineShaderManager *self) {
  self->useSimpleProgram();
}

//  void QOpenGLEngineShaderManager::useBlitProgram()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager14useBlitProgramEv(
    QOpenGLEngineShaderManager *self) {
  self->useBlitProgram();
}

//  void QOpenGLEngineShaderManager::setHasComplexGeometry(bool
//      hasComplexGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineShaderManager21setHasComplexGeometryEb(
    QOpenGLEngineShaderManager *self,
    bool hasComplexGeometry) {
  self->setHasComplexGeometry(hasComplexGeometry);
}

//  bool QOpenGLEngineShaderManager::hasComplexGeometry() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpenGLEngineShaderManager18hasComplexGeometryEv(
    const QOpenGLEngineShaderManager *self) {
  return self->hasComplexGeometry();
}

//  QOpenGLShaderProgram *QOpenGLEngineShaderManager::currentProgram()
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgram *ritual_ZN26QOpenGLEngineShaderManager14currentProgramEv(
    QOpenGLEngineShaderManager *self) {
  return self->currentProgram();
}

//  QOpenGLShaderProgram *QOpenGLEngineShaderManager::simpleProgram()
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgram *ritual_ZN26QOpenGLEngineShaderManager13simpleProgramEv(
    QOpenGLEngineShaderManager *self) {
  return self->simpleProgram();
}

//  QOpenGLShaderProgram *QOpenGLEngineShaderManager::blitProgram()
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgram *ritual_ZN26QOpenGLEngineShaderManager11blitProgramEv(
    QOpenGLEngineShaderManager *self) {
  return self->blitProgram();
}

//  a Python function taken by a CuteQOpenGLEngineShaderManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLEngineShaderManager(
    QOpenGLEngineShaderManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLEngineShaderManager *>(self)->take(key, call);
}
