//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopengl_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopengl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QSet>
#include <QtCore/QByteArray>

//  QOpenGLExtensionMatcher::QOpenGLExtensionMatcher()
extern "C" Q_DECL_EXPORT
QOpenGLExtensionMatcher *ritual_ZN23QOpenGLExtensionMatcherC1Ev() {
  return new QOpenGLExtensionMatcher();
}

//  bool QOpenGLExtensionMatcher::match(const QByteArray &extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QOpenGLExtensionMatcher5matchERK10QByteArray(
    const QOpenGLExtensionMatcher *self,
    const QByteArray *extension) {
  return self->match(*extension);
}

//  QSet<QByteArray> QOpenGLExtensionMatcher::extensions() const
extern "C" Q_DECL_EXPORT
QSet<QByteArray> *ritual_ZNK23QOpenGLExtensionMatcher10extensionsEv(
    const QOpenGLExtensionMatcher *self) {
  return new QSet<QByteArray>(self->extensions());
}

//  QOpenGLExtensionMatcher::~QOpenGLExtensionMatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLExtensionMatcherD1Ev(QOpenGLExtensionMatcher *self) {
  delete self;
}

//  a QSet<QByteArray> a ritual of QOpenGLExtensionMatcher gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLExtensionMatcher__QSet_QByteArray(
    QSet<QByteArray> *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
