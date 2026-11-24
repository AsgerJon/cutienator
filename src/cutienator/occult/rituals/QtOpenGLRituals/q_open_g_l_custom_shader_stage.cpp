//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcustomshaderstage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglcustomshaderstage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QOpenGLCustomShaderStage that Python can take functions over in. Every QOpenGLCustomShaderStage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOpenGLCustomShaderStageCall0)(const void *, QOpenGLShaderProgram *, int *);
class CuteQOpenGLCustomShaderStage : public QOpenGLCustomShaderStage {
public:
  using QOpenGLCustomShaderStage::QOpenGLCustomShaderStage;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QOpenGLCustomShaderStage11setUniformsEP20QOpenGLShaderProgram")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QOpenGLCustomShaderStage::setUniforms(QOpenGLShaderProgram *a0)
  void setUniforms(QOpenGLShaderProgram *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLCustomShaderStageCall0 call = reinterpret_cast<CuteQOpenGLCustomShaderStageCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QOpenGLCustomShaderStage::setUniforms(a0);
  }
};

//  QOpenGLCustomShaderStage::QOpenGLCustomShaderStage()
extern "C" Q_DECL_EXPORT
QOpenGLCustomShaderStage *ritual_ZN24QOpenGLCustomShaderStageC1Ev() {
  return new CuteQOpenGLCustomShaderStage();
}

//  QOpenGLCustomShaderStage::~QOpenGLCustomShaderStage()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLCustomShaderStageD1Ev(
    QOpenGLCustomShaderStage *self) {
  delete self;
}

//  void QOpenGLCustomShaderStage::setUniforms(QOpenGLShaderProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLCustomShaderStage11setUniformsEP20QOpenGLShaderProgram(
    QOpenGLCustomShaderStage *self,
    QOpenGLShaderProgram *a0) {
  self->setUniforms(a0);
}

//  void QOpenGLCustomShaderStage::setUniformsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLCustomShaderStage16setUniformsDirtyEv(
    QOpenGLCustomShaderStage *self) {
  self->setUniformsDirty();
}

//  bool QOpenGLCustomShaderStage::setOnPainter(QPainter *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLCustomShaderStage12setOnPainterEP8QPainter(
    QOpenGLCustomShaderStage *self,
    QPainter *a0) {
  return self->setOnPainter(a0);
}

//  void QOpenGLCustomShaderStage::removeFromPainter(QPainter *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLCustomShaderStage17removeFromPainterEP8QPainter(
    QOpenGLCustomShaderStage *self,
    QPainter *a0) {
  self->removeFromPainter(a0);
}

//  QByteArray QOpenGLCustomShaderStage::source() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QOpenGLCustomShaderStage6sourceEv(
    const QOpenGLCustomShaderStage *self) {
  return new QByteArray(self->source());
}

//  void QOpenGLCustomShaderStage::setInactive()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLCustomShaderStage11setInactiveEv(
    QOpenGLCustomShaderStage *self) {
  self->setInactive();
}

//  void QOpenGLCustomShaderStage::setSource(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLCustomShaderStage9setSourceERK10QByteArray(
    QOpenGLCustomShaderStage *self,
    const QByteArray *a0) {
  self->setSource(*a0);
}

//  a Python function taken by a CuteQOpenGLCustomShaderStage, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLCustomShaderStage(
    QOpenGLCustomShaderStage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLCustomShaderStage *>(self)->take(key, call);
}

//  void QOpenGLCustomShaderStage::setUniforms(QOpenGLShaderProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QOpenGLCustomShaderStage11setUniformsEP20QOpenGLShaderProgram(
    QOpenGLCustomShaderStage *self,
    QOpenGLShaderProgram *a0) {
  self->QOpenGLCustomShaderStage::setUniforms(a0);
}
