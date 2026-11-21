//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qopenglcontext.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QOpenGLContextGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QOpenGLContextGroup10metaObjectEv(
    const QOpenGLContextGroup *self) {
  return self->metaObject();
}

//  QString QOpenGLContextGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QOpenGLContextGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLContextGroup::tr(s, c, n));
}

//  QOpenGLContextGroup::~QOpenGLContextGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLContextGroupD1Ev(QOpenGLContextGroup *self) {
  delete self;
}

//  QOpenGLContextGroup *QOpenGLContextGroup::currentContextGroup()
extern "C" Q_DECL_EXPORT
QOpenGLContextGroup *ritual_ZN19QOpenGLContextGroup19currentContextGroupEv() {
  return QOpenGLContextGroup::currentContextGroup();
}
