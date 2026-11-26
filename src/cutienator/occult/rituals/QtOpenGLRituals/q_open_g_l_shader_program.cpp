//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglshaderprogram.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, rituals for functions the generator leaves out: 6. Kept as
//  it is when the generator runs again.
#include <QtOpenGL/qopenglshaderprogram.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qtransform.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QOpenGLShaderProgram that Python can take functions over in. Every QOpenGLShaderProgram
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQOpenGLShaderProgramCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLShaderProgramCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLShaderProgramCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderProgramCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderProgramCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderProgramCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderProgramCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLShaderProgramCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLShaderProgram : public QOpenGLShaderProgram {
public:
  using QOpenGLShaderProgram::QOpenGLShaderProgram;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QOpenGLShaderProgram4linkEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QOpenGLShaderProgram::link()
  bool link() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall0 call = reinterpret_cast<CuteQOpenGLShaderProgramCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLShaderProgram::link();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall1 call = reinterpret_cast<CuteQOpenGLShaderProgramCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall2 call = reinterpret_cast<CuteQOpenGLShaderProgramCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall3 call = reinterpret_cast<CuteQOpenGLShaderProgramCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall4 call = reinterpret_cast<CuteQOpenGLShaderProgramCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall5 call = reinterpret_cast<CuteQOpenGLShaderProgramCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall6 call = reinterpret_cast<CuteQOpenGLShaderProgramCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpenGLShaderProgramCall7 call = reinterpret_cast<CuteQOpenGLShaderProgramCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLShaderProgram::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QOpenGLShaderProgram10metaObjectEv(
    const QOpenGLShaderProgram *self) {
  return self->metaObject();
}

//  void *QOpenGLShaderProgram::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QOpenGLShaderProgram11qt_metacastEPKc(
    QOpenGLShaderProgram *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLShaderProgram::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QOpenGLShaderProgram11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLShaderProgram *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLShaderProgram::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QOpenGLShaderProgram2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLShaderProgram::tr(s, c, n));
}

//  QOpenGLShaderProgram::QOpenGLShaderProgram(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgram *ritual_ZN20QOpenGLShaderProgramC1EP7QObject(
    QObject *parent) {
  return new CuteQOpenGLShaderProgram(parent);
}

//  QOpenGLShaderProgram::~QOpenGLShaderProgram()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgramD1Ev(QOpenGLShaderProgram *self) {
  delete self;
}

//  bool QOpenGLShaderProgram::addShader(QOpenGLShader *shader)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram9addShaderEP13QOpenGLShader(
    QOpenGLShaderProgram *self,
    QOpenGLShader *shader) {
  return self->addShader(shader);
}

//  void QOpenGLShaderProgram::removeShader(QOpenGLShader *shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram12removeShaderEP13QOpenGLShader(
    QOpenGLShaderProgram *self,
    QOpenGLShader *shader) {
  self->removeShader(shader);
}

//  QList<QOpenGLShader *> QOpenGLShaderProgram::shaders() const
extern "C" Q_DECL_EXPORT
QList<QOpenGLShader *> *ritual_ZNK20QOpenGLShaderProgram7shadersEv(
    const QOpenGLShaderProgram *self) {
  return new QList<QOpenGLShader *>(self->shaders());
}

//  bool
//      QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderTy
//      pe type, const char *source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceCodeE6QFlagsIN13QOpenGLShader13ShaderTypeBitEEPKc(
    QOpenGLShaderProgram *self,
    int type,
    const char *source) {
  return self->addShaderFromSourceCode(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      source);
}

//  bool
//      QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderTy
//      pe type, const QByteArray &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceCodeE6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK10QByteArray(
    QOpenGLShaderProgram *self,
    int type,
    const QByteArray *source) {
  return self->addShaderFromSourceCode(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      *source);
}

//  bool
//      QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderTy
//      pe type, const QString &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceCodeE6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK7QString(
    QOpenGLShaderProgram *self,
    int type,
    const QString *source) {
  return self->addShaderFromSourceCode(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      *source);
}

//  bool
//      QOpenGLShaderProgram::addShaderFromSourceFile(QOpenGLShader::ShaderTy
//      pe type, const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceFileE6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK7QString(
    QOpenGLShaderProgram *self,
    int type,
    const QString *fileName) {
  return self->addShaderFromSourceFile(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      *fileName);
}

//  bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader
//      ::ShaderType type, const char *source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceCodeE6QFlagsIN13QOpenGLShader13ShaderTypeBitEEPKc(
    QOpenGLShaderProgram *self,
    int type,
    const char *source) {
  return self->addCacheableShaderFromSourceCode(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      source);
}

//  bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader
//      ::ShaderType type, const QByteArray &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceCodeE6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK10QByteArray(
    QOpenGLShaderProgram *self,
    int type,
    const QByteArray *source) {
  return self->addCacheableShaderFromSourceCode(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      *source);
}

//  bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader
//      ::ShaderType type, const QString &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceCodeE6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK7QString(
    QOpenGLShaderProgram *self,
    int type,
    const QString *source) {
  return self->addCacheableShaderFromSourceCode(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      *source);
}

//  bool QOpenGLShaderProgram::addCacheableShaderFromSourceFile(QOpenGLShader
//      ::ShaderType type, const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceFileE6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK7QString(
    QOpenGLShaderProgram *self,
    int type,
    const QString *fileName) {
  return self->addCacheableShaderFromSourceFile(
      QFlags<QOpenGLShader::ShaderTypeBit>::fromInt(type),
      *fileName);
}

//  void QOpenGLShaderProgram::removeAllShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram16removeAllShadersEv(
    QOpenGLShaderProgram *self) {
  self->removeAllShaders();
}

//  bool QOpenGLShaderProgram::link()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram4linkEv(QOpenGLShaderProgram *self) {
  return self->link();
}

//  bool QOpenGLShaderProgram::isLinked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpenGLShaderProgram8isLinkedEv(
    const QOpenGLShaderProgram *self) {
  return self->isLinked();
}

//  QString QOpenGLShaderProgram::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QOpenGLShaderProgram3logEv(
    const QOpenGLShaderProgram *self) {
  return new QString(self->log());
}

//  bool QOpenGLShaderProgram::bind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram4bindEv(QOpenGLShaderProgram *self) {
  return self->bind();
}

//  void QOpenGLShaderProgram::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram7releaseEv(QOpenGLShaderProgram *self) {
  self->release();
}

//  bool QOpenGLShaderProgram::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram6createEv(QOpenGLShaderProgram *self) {
  return self->create();
}

//  GLuint QOpenGLShaderProgram::programId() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK20QOpenGLShaderProgram9programIdEv(
    const QOpenGLShaderProgram *self) {
  return self->programId();
}

//  int QOpenGLShaderProgram::maxGeometryOutputVertices() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram25maxGeometryOutputVerticesEv(
    const QOpenGLShaderProgram *self) {
  return self->maxGeometryOutputVertices();
}

//  void QOpenGLShaderProgram::setPatchVertexCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram19setPatchVertexCountEi(
    QOpenGLShaderProgram *self,
    int count) {
  self->setPatchVertexCount(count);
}

//  int QOpenGLShaderProgram::patchVertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram16patchVertexCountEv(
    const QOpenGLShaderProgram *self) {
  return self->patchVertexCount();
}

//  void QOpenGLShaderProgram::setDefaultOuterTessellationLevels(const
//      QList<float> &levels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram33setDefaultOuterTessellationLevelsERK5QListIfE(
    QOpenGLShaderProgram *self,
    const QList<float> *levels) {
  self->setDefaultOuterTessellationLevels(*levels);
}

//  QList<float> QOpenGLShaderProgram::defaultOuterTessellationLevels() const
extern "C" Q_DECL_EXPORT
QList<float> *ritual_ZNK20QOpenGLShaderProgram30defaultOuterTessellationLevelsEv(
    const QOpenGLShaderProgram *self) {
  return new QList<float>(self->defaultOuterTessellationLevels());
}

//  void QOpenGLShaderProgram::setDefaultInnerTessellationLevels(const
//      QList<float> &levels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram33setDefaultInnerTessellationLevelsERK5QListIfE(
    QOpenGLShaderProgram *self,
    const QList<float> *levels) {
  self->setDefaultInnerTessellationLevels(*levels);
}

//  QList<float> QOpenGLShaderProgram::defaultInnerTessellationLevels() const
extern "C" Q_DECL_EXPORT
QList<float> *ritual_ZNK20QOpenGLShaderProgram30defaultInnerTessellationLevelsEv(
    const QOpenGLShaderProgram *self) {
  return new QList<float>(self->defaultInnerTessellationLevels());
}

//  void QOpenGLShaderProgram::bindAttributeLocation(const char *name, int
//      location)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram21bindAttributeLocationEPKci(
    QOpenGLShaderProgram *self,
    const char *name,
    int location) {
  self->bindAttributeLocation(name, location);
}

//  void QOpenGLShaderProgram::bindAttributeLocation(const QByteArray &name,
//      int location)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram21bindAttributeLocationERK10QByteArrayi(
    QOpenGLShaderProgram *self,
    const QByteArray *name,
    int location) {
  self->bindAttributeLocation(*name, location);
}

//  void QOpenGLShaderProgram::bindAttributeLocation(const QString &name, int
//      location)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram21bindAttributeLocationERK7QStringi(
    QOpenGLShaderProgram *self,
    const QString *name,
    int location) {
  self->bindAttributeLocation(*name, location);
}

//  int QOpenGLShaderProgram::attributeLocation(const char *name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram17attributeLocationEPKc(
    const QOpenGLShaderProgram *self,
    const char *name) {
  return self->attributeLocation(name);
}

//  int QOpenGLShaderProgram::attributeLocation(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram17attributeLocationERK10QByteArray(
    const QOpenGLShaderProgram *self,
    const QByteArray *name) {
  return self->attributeLocation(*name);
}

//  int QOpenGLShaderProgram::attributeLocation(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram17attributeLocationERK7QString(
    const QOpenGLShaderProgram *self,
    const QString *name) {
  return self->attributeLocation(*name);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEif(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat value) {
  self->setAttributeValue(location, value);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiff(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat x,
    GLfloat y) {
  self->setAttributeValue(location, x, y);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEifff(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->setAttributeValue(location, x, y, z);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiffff(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->setAttributeValue(location, x, y, z, w);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, const
//      QVector2D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK9QVector2D(
    QOpenGLShaderProgram *self,
    int location,
    const QVector2D *value) {
  self->setAttributeValue(location, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, const
//      QVector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK9QVector3D(
    QOpenGLShaderProgram *self,
    int location,
    const QVector3D *value) {
  self->setAttributeValue(location, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, const
//      QVector4D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK9QVector4D(
    QOpenGLShaderProgram *self,
    int location,
    const QVector4D *value) {
  self->setAttributeValue(location, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, const QColor
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK6QColor(
    QOpenGLShaderProgram *self,
    int location,
    const QColor *value) {
  self->setAttributeValue(location, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(int location, const GLfloat
//      *values, int columns, int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiPKfii(
    QOpenGLShaderProgram *self,
    int location,
    const GLfloat *values,
    int columns,
    int rows) {
  self->setAttributeValue(location, values, columns, rows);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcf(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat value) {
  self->setAttributeValue(name, value);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcff(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat x,
    GLfloat y) {
  self->setAttributeValue(name, x, y);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcfff(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->setAttributeValue(name, x, y, z);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcffff(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->setAttributeValue(name, x, y, z, w);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
//      QVector2D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK9QVector2D(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector2D *value) {
  self->setAttributeValue(name, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
//      QVector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK9QVector3D(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector3D *value) {
  self->setAttributeValue(name, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
//      QVector4D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK9QVector4D(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector4D *value) {
  self->setAttributeValue(name, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
//      QColor &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK6QColor(
    QOpenGLShaderProgram *self,
    const char *name,
    const QColor *value) {
  self->setAttributeValue(name, *value);
}

//  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
//      GLfloat *values, int columns, int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcPKfii(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLfloat *values,
    int columns,
    int rows) {
  self->setAttributeValue(name, values, columns, rows);
}

//  void QOpenGLShaderProgram::setAttributeArray(int location, const GLfloat
//      *values, int tupleSize, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPKfii(
    QOpenGLShaderProgram *self,
    int location,
    const GLfloat *values,
    int tupleSize,
    int stride) {
  self->setAttributeArray(location, values, tupleSize, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(int location, const
//      QVector2D *values, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPK9QVector2Di(
    QOpenGLShaderProgram *self,
    int location,
    const QVector2D *values,
    int stride) {
  self->setAttributeArray(location, values, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(int location, const
//      QVector3D *values, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPK9QVector3Di(
    QOpenGLShaderProgram *self,
    int location,
    const QVector3D *values,
    int stride) {
  self->setAttributeArray(location, values, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(int location, const
//      QVector4D *values, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPK9QVector4Di(
    QOpenGLShaderProgram *self,
    int location,
    const QVector4D *values,
    int stride) {
  self->setAttributeArray(location, values, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(int location, GLenum type,
//      const void *values, int tupleSize, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEijPKvii(
    QOpenGLShaderProgram *self,
    int location,
    GLenum type,
    const void *values,
    int tupleSize,
    int stride) {
  self->setAttributeArray(location, type, values, tupleSize, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
//      GLfloat *values, int tupleSize, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPKfii(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLfloat *values,
    int tupleSize,
    int stride) {
  self->setAttributeArray(name, values, tupleSize, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
//      QVector2D *values, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPK9QVector2Di(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector2D *values,
    int stride) {
  self->setAttributeArray(name, values, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
//      QVector3D *values, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPK9QVector3Di(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector3D *values,
    int stride) {
  self->setAttributeArray(name, values, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
//      QVector4D *values, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPK9QVector4Di(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector4D *values,
    int stride) {
  self->setAttributeArray(name, values, stride);
}

//  void QOpenGLShaderProgram::setAttributeArray(const char *name, GLenum
//      type, const void *values, int tupleSize, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcjPKvii(
    QOpenGLShaderProgram *self,
    const char *name,
    GLenum type,
    const void *values,
    int tupleSize,
    int stride) {
  self->setAttributeArray(name, type, values, tupleSize, stride);
}

//  void QOpenGLShaderProgram::setAttributeBuffer(int location, GLenum type,
//      int offset, int tupleSize, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram18setAttributeBufferEijiii(
    QOpenGLShaderProgram *self,
    int location,
    GLenum type,
    int offset,
    int tupleSize,
    int stride) {
  self->setAttributeBuffer(location, type, offset, tupleSize, stride);
}

//  void QOpenGLShaderProgram::setAttributeBuffer(const char *name, GLenum
//      type, int offset, int tupleSize, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram18setAttributeBufferEPKcjiii(
    QOpenGLShaderProgram *self,
    const char *name,
    GLenum type,
    int offset,
    int tupleSize,
    int stride) {
  self->setAttributeBuffer(name, type, offset, tupleSize, stride);
}

//  void QOpenGLShaderProgram::enableAttributeArray(int location)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20enableAttributeArrayEi(
    QOpenGLShaderProgram *self,
    int location) {
  self->enableAttributeArray(location);
}

//  void QOpenGLShaderProgram::enableAttributeArray(const char *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20enableAttributeArrayEPKc(
    QOpenGLShaderProgram *self,
    const char *name) {
  self->enableAttributeArray(name);
}

//  void QOpenGLShaderProgram::disableAttributeArray(int location)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram21disableAttributeArrayEi(
    QOpenGLShaderProgram *self,
    int location) {
  self->disableAttributeArray(location);
}

//  void QOpenGLShaderProgram::disableAttributeArray(const char *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram21disableAttributeArrayEPKc(
    QOpenGLShaderProgram *self,
    const char *name) {
  self->disableAttributeArray(name);
}

//  int QOpenGLShaderProgram::uniformLocation(const char *name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram15uniformLocationEPKc(
    const QOpenGLShaderProgram *self,
    const char *name) {
  return self->uniformLocation(name);
}

//  int QOpenGLShaderProgram::uniformLocation(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram15uniformLocationERK10QByteArray(
    const QOpenGLShaderProgram *self,
    const QByteArray *name) {
  return self->uniformLocation(*name);
}

//  int QOpenGLShaderProgram::uniformLocation(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QOpenGLShaderProgram15uniformLocationERK7QString(
    const QOpenGLShaderProgram *self,
    const QString *name) {
  return self->uniformLocation(*name);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEif(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat value) {
  self->setUniformValue(location, value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEii(
    QOpenGLShaderProgram *self,
    int location,
    GLint value) {
  self->setUniformValue(location, value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, GLuint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEij(
    QOpenGLShaderProgram *self,
    int location,
    GLuint value) {
  self->setUniformValue(location, value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiff(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat x,
    GLfloat y) {
  self->setUniformValue(location, x, y);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEifff(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->setUniformValue(location, x, y, z);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiffff(
    QOpenGLShaderProgram *self,
    int location,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->setUniformValue(location, x, y, z, w);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QVector2D
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK9QVector2D(
    QOpenGLShaderProgram *self,
    int location,
    const QVector2D *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QVector3D
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK9QVector3D(
    QOpenGLShaderProgram *self,
    int location,
    const QVector3D *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QVector4D
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK9QVector4D(
    QOpenGLShaderProgram *self,
    int location,
    const QVector4D *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK6QColor(
    QOpenGLShaderProgram *self,
    int location,
    const QColor *color) {
  self->setUniformValue(location, *color);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QPoint
//      &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK6QPoint(
    QOpenGLShaderProgram *self,
    int location,
    const QPoint *point) {
  self->setUniformValue(location, *point);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK7QPointF(
    QOpenGLShaderProgram *self,
    int location,
    const QPointF *point) {
  self->setUniformValue(location, *point);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QSize
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK5QSize(
    QOpenGLShaderProgram *self,
    int location,
    const QSize *size) {
  self->setUniformValue(location, *size);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QSizeF
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK6QSizeF(
    QOpenGLShaderProgram *self,
    int location,
    const QSizeF *size) {
  self->setUniformValue(location, *size);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix2x2
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi2ELi2EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix2x2 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix2x3
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi2ELi3EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix2x3 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix2x4
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi2ELi4EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix2x4 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix3x2
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi3ELi2EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix3x2 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix3x3
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi3ELi3EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix3x3 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix3x4
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi3ELi4EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix3x4 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix4x2
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi4ELi2EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix4x2 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix4x3
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK14QGenericMatrixILi4ELi3EfE(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix4x3 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QMatrix4x4
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK10QMatrix4x4(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix4x4 *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const QTransform
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK10QTransform(
    QOpenGLShaderProgram *self,
    int location,
    const QTransform *value) {
  self->setUniformValue(location, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcf(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat value) {
  self->setUniformValue(name, value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, GLint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKci(
    QOpenGLShaderProgram *self,
    const char *name,
    GLint value) {
  self->setUniformValue(name, value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, GLuint
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcj(
    QOpenGLShaderProgram *self,
    const char *name,
    GLuint value) {
  self->setUniformValue(name, value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat x,
//      GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcff(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat x,
    GLfloat y) {
  self->setUniformValue(name, x, y);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat x,
//      GLfloat y, GLfloat z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcfff(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat x,
    GLfloat y,
    GLfloat z) {
  self->setUniformValue(name, x, y, z);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat x,
//      GLfloat y, GLfloat z, GLfloat w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcffff(
    QOpenGLShaderProgram *self,
    const char *name,
    GLfloat x,
    GLfloat y,
    GLfloat z,
    GLfloat w) {
  self->setUniformValue(name, x, y, z, w);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QVector2D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK9QVector2D(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector2D *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QVector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK9QVector3D(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector3D *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QVector4D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK9QVector4D(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector4D *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK6QColor(
    QOpenGLShaderProgram *self,
    const char *name,
    const QColor *color) {
  self->setUniformValue(name, *color);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const QPoint
//      &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK6QPoint(
    QOpenGLShaderProgram *self,
    const char *name,
    const QPoint *point) {
  self->setUniformValue(name, *point);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK7QPointF(
    QOpenGLShaderProgram *self,
    const char *name,
    const QPointF *point) {
  self->setUniformValue(name, *point);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const QSize
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK5QSize(
    QOpenGLShaderProgram *self,
    const char *name,
    const QSize *size) {
  self->setUniformValue(name, *size);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const QSizeF
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK6QSizeF(
    QOpenGLShaderProgram *self,
    const char *name,
    const QSizeF *size) {
  self->setUniformValue(name, *size);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix2x2 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi2ELi2EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix2x2 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix2x3 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi2ELi3EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix2x3 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix2x4 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi2ELi4EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix2x4 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix3x2 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi3ELi2EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix3x2 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix3x3 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi3ELi3EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix3x3 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix3x4 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi3ELi4EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix3x4 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix4x2 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi4ELi2EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix4x2 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix4x3 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK14QGenericMatrixILi4ELi3EfE(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix4x3 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QMatrix4x4 &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK10QMatrix4x4(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix4x4 *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      QTransform &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK10QTransform(
    QOpenGLShaderProgram *self,
    const char *name,
    const QTransform *value) {
  self->setUniformValue(name, *value);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      GLfloat *values, int count, int tupleSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPKfii(
    QOpenGLShaderProgram *self,
    int location,
    const GLfloat *values,
    int count,
    int tupleSize) {
  self->setUniformValueArray(location, values, count, tupleSize);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const GLint
//      *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPKii(
    QOpenGLShaderProgram *self,
    int location,
    const GLint *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      GLuint *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPKji(
    QOpenGLShaderProgram *self,
    int location,
    const GLuint *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QVector2D *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK9QVector2Di(
    QOpenGLShaderProgram *self,
    int location,
    const QVector2D *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QVector3D *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK9QVector3Di(
    QOpenGLShaderProgram *self,
    int location,
    const QVector3D *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QVector4D *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK9QVector4Di(
    QOpenGLShaderProgram *self,
    int location,
    const QVector4D *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix2x2 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi2ELi2EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix2x2 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix2x3 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi2ELi3EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix2x3 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix2x4 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi2ELi4EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix2x4 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix3x2 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi3ELi2EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix3x2 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix3x3 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi3ELi3EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix3x3 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix3x4 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi3ELi4EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix3x4 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix4x2 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi4ELi2EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix4x2 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix4x3 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK14QGenericMatrixILi4ELi3EfEi(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix4x3 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(int location, const
//      QMatrix4x4 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK10QMatrix4x4i(
    QOpenGLShaderProgram *self,
    int location,
    const QMatrix4x4 *values,
    int count) {
  self->setUniformValueArray(location, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      GLfloat *values, int count, int tupleSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPKfii(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLfloat *values,
    int count,
    int tupleSize) {
  self->setUniformValueArray(name, values, count, tupleSize);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      GLint *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPKii(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLint *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      GLuint *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPKji(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLuint *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QVector2D *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK9QVector2Di(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector2D *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QVector3D *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK9QVector3Di(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector3D *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QVector4D *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK9QVector4Di(
    QOpenGLShaderProgram *self,
    const char *name,
    const QVector4D *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix2x2 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi2ELi2EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix2x2 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix2x3 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi2ELi3EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix2x3 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix2x4 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi2ELi4EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix2x4 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix3x2 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi3ELi2EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix3x2 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix3x3 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi3ELi3EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix3x3 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix3x4 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi3ELi4EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix3x4 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix4x2 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi4ELi2EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix4x2 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix4x3 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK14QGenericMatrixILi4ELi3EfEi(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix4x3 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  void QOpenGLShaderProgram::setUniformValueArray(const char *name, const
//      QMatrix4x4 *values, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK10QMatrix4x4i(
    QOpenGLShaderProgram *self,
    const char *name,
    const QMatrix4x4 *values,
    int count) {
  self->setUniformValueArray(name, values, count);
}

//  bool QOpenGLShaderProgram::hasOpenGLShaderPrograms(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram23hasOpenGLShaderProgramsEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLShaderProgram::hasOpenGLShaderPrograms(context);
}

//  void QOpenGLShaderProgram::shaderDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15shaderDestroyedEv(
    QOpenGLShaderProgram *self) {
  self->shaderDestroyed();
}

//  QOpenGLShaderProgramPrivate *QOpenGLShaderProgram::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgramPrivate *ritual_ZN20QOpenGLShaderProgram6d_funcEv(
    QOpenGLShaderProgram *self) {
  return self->d_func();
}

//  const QOpenGLShaderProgramPrivate *QOpenGLShaderProgram::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLShaderProgramPrivate *ritual_ZNK20QOpenGLShaderProgram6d_funcEv(
    const QOpenGLShaderProgram *self) {
  return self->d_func();
}

//  bool QOpenGLShaderProgram::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QOpenGLShaderProgram4initEv(QOpenGLShaderProgram *self) {
  return self->init();
}

//  a Python function taken by a CuteQOpenGLShaderProgram, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLShaderProgram(
    QOpenGLShaderProgram *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLShaderProgram *>(self)->take(key, call);
}

//  bool QOpenGLShaderProgram::link()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QOpenGLShaderProgram4linkEv(QOpenGLShaderProgram *self) {
  return self->QOpenGLShaderProgram::link();
}

//  a QList<float> a ritual of QOpenGLShaderProgram gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLShaderProgram__QList_float(QList<float> *self) {
  delete self;
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const GLfloat
//      value[2][2])
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiPA2_Kf(
    QOpenGLShaderProgram *self,
    int location,
    const GLfloat *value) {
  self->setUniformValue(
      location, reinterpret_cast<const GLfloat (*)[2]>(value));
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      GLfloat value[2][2])
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcPA2_Kf(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLfloat *value) {
  self->setUniformValue(
      name, reinterpret_cast<const GLfloat (*)[2]>(value));
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const GLfloat
//      value[3][3])
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiPA3_Kf(
    QOpenGLShaderProgram *self,
    int location,
    const GLfloat *value) {
  self->setUniformValue(
      location, reinterpret_cast<const GLfloat (*)[3]>(value));
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      GLfloat value[3][3])
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcPA3_Kf(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLfloat *value) {
  self->setUniformValue(
      name, reinterpret_cast<const GLfloat (*)[3]>(value));
}

//  void QOpenGLShaderProgram::setUniformValue(int location, const GLfloat
//      value[4][4])
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEiPA4_Kf(
    QOpenGLShaderProgram *self,
    int location,
    const GLfloat *value) {
  self->setUniformValue(
      location, reinterpret_cast<const GLfloat (*)[4]>(value));
}

//  void QOpenGLShaderProgram::setUniformValue(const char *name, const
//      GLfloat value[4][4])
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcPA4_Kf(
    QOpenGLShaderProgram *self,
    const char *name,
    const GLfloat *value) {
  self->setUniformValue(
      name, reinterpret_cast<const GLfloat (*)[4]>(value));
}
