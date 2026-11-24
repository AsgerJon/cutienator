//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglshaderprogram.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qopenglshaderprogram.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpenGLShader that Python can take functions over in. Every QOpenGLShader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLShaderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLShaderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLShader : public QOpenGLShader {
public:
  using QOpenGLShader::QOpenGLShader;
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
      CuteQOpenGLShaderCall0 call = reinterpret_cast<CuteQOpenGLShaderCall0>(taken[0]);
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
      CuteQOpenGLShaderCall1 call = reinterpret_cast<CuteQOpenGLShaderCall1>(taken[1]);
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
      CuteQOpenGLShaderCall2 call = reinterpret_cast<CuteQOpenGLShaderCall2>(taken[2]);
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
      CuteQOpenGLShaderCall3 call = reinterpret_cast<CuteQOpenGLShaderCall3>(taken[3]);
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
      CuteQOpenGLShaderCall4 call = reinterpret_cast<CuteQOpenGLShaderCall4>(taken[4]);
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
      CuteQOpenGLShaderCall5 call = reinterpret_cast<CuteQOpenGLShaderCall5>(taken[5]);
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
      CuteQOpenGLShaderCall6 call = reinterpret_cast<CuteQOpenGLShaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLShader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QOpenGLShader10metaObjectEv(
    const QOpenGLShader *self) {
  return self->metaObject();
}

//  QString QOpenGLShader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QOpenGLShader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLShader::tr(s, c, n));
}

//  QOpenGLShader::QOpenGLShader(QOpenGLShader::ShaderType type, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QOpenGLShader *ritual_ZN13QOpenGLShaderC1E6QFlagsINS_13ShaderTypeBitEEP7QObject(
    int type,
    QObject *parent) {
  return new CuteQOpenGLShader(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      parent);
}

//  QOpenGLShader::~QOpenGLShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLShaderD1Ev(QOpenGLShader *self) {
  delete self;
}

//  QOpenGLShader::ShaderType QOpenGLShader::shaderType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QOpenGLShader10shaderTypeEv(const QOpenGLShader *self) {
  return static_cast<int>(self->shaderType().toInt());
}

//  bool QOpenGLShader::compileSourceCode(const char *source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLShader17compileSourceCodeEPKc(
    QOpenGLShader *self,
    const char *source) {
  return self->compileSourceCode(source);
}

//  bool QOpenGLShader::compileSourceCode(const QByteArray &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLShader17compileSourceCodeERK10QByteArray(
    QOpenGLShader *self,
    const QByteArray *source) {
  return self->compileSourceCode(*source);
}

//  bool QOpenGLShader::compileSourceCode(const QString &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLShader17compileSourceCodeERK7QString(
    QOpenGLShader *self,
    const QString *source) {
  return self->compileSourceCode(*source);
}

//  bool QOpenGLShader::compileSourceFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLShader17compileSourceFileERK7QString(
    QOpenGLShader *self,
    const QString *fileName) {
  return self->compileSourceFile(*fileName);
}

//  QByteArray QOpenGLShader::sourceCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QOpenGLShader10sourceCodeEv(
    const QOpenGLShader *self) {
  return new QByteArray(self->sourceCode());
}

//  bool QOpenGLShader::isCompiled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpenGLShader10isCompiledEv(const QOpenGLShader *self) {
  return self->isCompiled();
}

//  QString QOpenGLShader::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QOpenGLShader3logEv(const QOpenGLShader *self) {
  return new QString(self->log());
}

//  bool QOpenGLShader::hasOpenGLShaders(ShaderType type, QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLShader16hasOpenGLShadersE6QFlagsINS_13ShaderTypeBitEEP14QOpenGLContext(
    int type,
    QOpenGLContext *context) {
  return QOpenGLShader::hasOpenGLShaders(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      context);
}

//  a Python function taken by a CuteQOpenGLShader, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLShader(
    QOpenGLShader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLShader *>(self)->take(key, call);
}

//  QList<QOpenGLShader *>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpenGLShader *> *ritual_list_make_QOpenGLShader_ptr() {
  return new QList<QOpenGLShader *>();
}

//  void QList<QOpenGLShader *>::append(const QOpenGLShader * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpenGLShader_ptr(
    QList<QOpenGLShader *> *self,
    QOpenGLShader *element) {
  self->append(element);
}

//  qsizetype QList<QOpenGLShader *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpenGLShader_ptr(
    const QList<QOpenGLShader *> *self) {
  return self->size();
}

//  const QOpenGLShader * &QList<QOpenGLShader *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpenGLShader *ritual_list_at_QOpenGLShader_ptr(
    const QList<QOpenGLShader *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QOpenGLShader *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpenGLShader_ptr(QList<QOpenGLShader *> *self) {
  delete self;
}
