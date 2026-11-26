//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qshaderprogram.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qshaderprogram.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QShaderProgram that Python can take functions over in. Every Qt3DRender::QShaderProgram
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderProgramCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderProgramCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QShaderProgram : public Qt3DRender::QShaderProgram {
public:
  using Qt3DRender::QShaderProgram::QShaderProgram;
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
      CuteQt3DRender_QShaderProgramCall0 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall0>(taken[0]);
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
      CuteQt3DRender_QShaderProgramCall1 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall1>(taken[1]);
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
      CuteQt3DRender_QShaderProgramCall2 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall2>(taken[2]);
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
      CuteQt3DRender_QShaderProgramCall3 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall3>(taken[3]);
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
      CuteQt3DRender_QShaderProgramCall4 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall4>(taken[4]);
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
      CuteQt3DRender_QShaderProgramCall5 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall5>(taken[5]);
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
      CuteQt3DRender_QShaderProgramCall6 call = reinterpret_cast<CuteQt3DRender_QShaderProgramCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QShaderProgram::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QShaderProgram10metaObjectEv(
    const Qt3DRender::QShaderProgram *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QShaderProgram::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender14QShaderProgram11qt_metacastEPKc(
    Qt3DRender::QShaderProgram *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QShaderProgram::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender14QShaderProgram11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QShaderProgram *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QShaderProgram::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender14QShaderProgram2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QShaderProgram::tr(s, c, n));
}

//  Qt3DRender::QShaderProgram::QShaderProgram(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram *ritual_ZN10Qt3DRender14QShaderProgramC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderProgram(parent);
}

//  Qt3DRender::QShaderProgram::~QShaderProgram()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgramD1Ev(
    Qt3DRender::QShaderProgram *self) {
  delete self;
}

//  QByteArray Qt3DRender::QShaderProgram::vertexShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram16vertexShaderCodeEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QByteArray(self->vertexShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgram::tessellationControlShaderCode()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram29tessellationControlShaderCodeEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QByteArray(self->tessellationControlShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgram::tessellationEvaluationShaderCode()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram32tessellationEvaluationShaderCodeEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QByteArray(self->tessellationEvaluationShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgram::geometryShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram18geometryShaderCodeEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QByteArray(self->geometryShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgram::fragmentShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram18fragmentShaderCodeEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QByteArray(self->fragmentShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgram::computeShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram17computeShaderCodeEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QByteArray(self->computeShaderCode());
}

//  void Qt3DRender::QShaderProgram::setShaderCode(ShaderType type, const
//      QByteArray &shaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram13setShaderCodeENS0_10ShaderTypeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    Qt3DRender::QShaderProgram::ShaderType type,
    const QByteArray *shaderCode) {
  self->setShaderCode(type, *shaderCode);
}

//  QByteArray Qt3DRender::QShaderProgram::shaderCode(ShaderType type) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender14QShaderProgram10shaderCodeENS0_10ShaderTypeE(
    const Qt3DRender::QShaderProgram *self,
    Qt3DRender::QShaderProgram::ShaderType type) {
  return new QByteArray(self->shaderCode(type));
}

//  QString Qt3DRender::QShaderProgram::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender14QShaderProgram3logEv(
    const Qt3DRender::QShaderProgram *self) {
  return new QString(self->log());
}

//  Status Qt3DRender::QShaderProgram::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram::Status ritual_ZNK10Qt3DRender14QShaderProgram6statusEv(
    const Qt3DRender::QShaderProgram *self) {
  return self->status();
}

//  void Qt3DRender::QShaderProgram::setFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram9setFormatENS0_6FormatE(
    Qt3DRender::QShaderProgram *self,
    Qt3DRender::QShaderProgram::Format format) {
  self->setFormat(format);
}

//  Format Qt3DRender::QShaderProgram::format() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram::Format ritual_ZNK10Qt3DRender14QShaderProgram6formatEv(
    const Qt3DRender::QShaderProgram *self) {
  return self->format();
}

//  QByteArray Qt3DRender::QShaderProgram::loadSource(const QUrl &sourceUrl)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10Qt3DRender14QShaderProgram10loadSourceERK4QUrl(
    const QUrl *sourceUrl) {
  return new QByteArray(Qt3DRender::QShaderProgram::loadSource(*sourceUrl));
}

//  void Qt3DRender::QShaderProgram::setVertexShaderCode(const QByteArray
//      &vertexShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram19setVertexShaderCodeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *vertexShaderCode) {
  self->setVertexShaderCode(*vertexShaderCode);
}

//  void Qt3DRender::QShaderProgram::setTessellationControlShaderCode(const
//      QByteArray &tessellationControlShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram32setTessellationControlShaderCodeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *tessellationControlShaderCode) {
  self->setTessellationControlShaderCode(*tessellationControlShaderCode);
}

//  void
//      Qt3DRender::QShaderProgram::setTessellationEvaluationShaderCode(const
//      QByteArray &tessellationEvaluationShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram35setTessellationEvaluationShaderCodeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *tessellationEvaluationShaderCode) {
  self->setTessellationEvaluationShaderCode(
      *tessellationEvaluationShaderCode);
}

//  void Qt3DRender::QShaderProgram::setGeometryShaderCode(const QByteArray
//      &geometryShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram21setGeometryShaderCodeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *geometryShaderCode) {
  self->setGeometryShaderCode(*geometryShaderCode);
}

//  void Qt3DRender::QShaderProgram::setFragmentShaderCode(const QByteArray
//      &fragmentShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram21setFragmentShaderCodeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *fragmentShaderCode) {
  self->setFragmentShaderCode(*fragmentShaderCode);
}

//  void Qt3DRender::QShaderProgram::setComputeShaderCode(const QByteArray
//      &computeShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram20setComputeShaderCodeERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *computeShaderCode) {
  self->setComputeShaderCode(*computeShaderCode);
}

//  void Qt3DRender::QShaderProgram::vertexShaderCodeChanged(const QByteArray
//      &vertexShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram23vertexShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *vertexShaderCode) {
  self->vertexShaderCodeChanged(*vertexShaderCode);
}

//  void
//      Qt3DRender::QShaderProgram::tessellationControlShaderCodeChanged(cons
//      t QByteArray &tessellationControlShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram36tessellationControlShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *tessellationControlShaderCode) {
  self->tessellationControlShaderCodeChanged(*tessellationControlShaderCode);
}

//  void
//      Qt3DRender::QShaderProgram::tessellationEvaluationShaderCodeChanged(c
//      onst QByteArray &tessellationEvaluationShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram39tessellationEvaluationShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *tessellationEvaluationShaderCode) {
  self->tessellationEvaluationShaderCodeChanged(
      *tessellationEvaluationShaderCode);
}

//  void Qt3DRender::QShaderProgram::geometryShaderCodeChanged(const
//      QByteArray &geometryShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram25geometryShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *geometryShaderCode) {
  self->geometryShaderCodeChanged(*geometryShaderCode);
}

//  void Qt3DRender::QShaderProgram::fragmentShaderCodeChanged(const
//      QByteArray &fragmentShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram25fragmentShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *fragmentShaderCode) {
  self->fragmentShaderCodeChanged(*fragmentShaderCode);
}

//  void Qt3DRender::QShaderProgram::computeShaderCodeChanged(const
//      QByteArray &computeShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram24computeShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgram *self,
    const QByteArray *computeShaderCode) {
  self->computeShaderCodeChanged(*computeShaderCode);
}

//  void Qt3DRender::QShaderProgram::logChanged(const QString &log)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram10logChangedERK7QString(
    Qt3DRender::QShaderProgram *self,
    const QString *log) {
  self->logChanged(*log);
}

//  void Qt3DRender::QShaderProgram::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram13statusChangedENS0_6StatusE(
    Qt3DRender::QShaderProgram *self,
    Qt3DRender::QShaderProgram::Status status) {
  self->statusChanged(status);
}

//  void Qt3DRender::QShaderProgram::formatChanged(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QShaderProgram13formatChangedENS0_6FormatE(
    Qt3DRender::QShaderProgram *self,
    Qt3DRender::QShaderProgram::Format format) {
  self->formatChanged(format);
}

//  Qt3DRender::QShaderProgram::QShaderProgram(QShaderProgramPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram *ritual_ZN10Qt3DRender14QShaderProgramC1ERNS_21QShaderProgramPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QShaderProgramPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderProgram(*dd, parent);
}

//  QShaderProgramPrivate *Qt3DRender::QShaderProgram::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgramPrivate *ritual_ZN10Qt3DRender14QShaderProgram6d_funcEv(
    Qt3DRender::QShaderProgram *self) {
  return self->d_func();
}

//  const QShaderProgramPrivate *Qt3DRender::QShaderProgram::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QShaderProgramPrivate *ritual_ZNK10Qt3DRender14QShaderProgram6d_funcEv(
    const Qt3DRender::QShaderProgram *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QShaderProgram, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QShaderProgram(
    Qt3DRender::QShaderProgram *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QShaderProgram *>(self)->take(key, call);
}
