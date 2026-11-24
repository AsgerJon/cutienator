//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGles2RenderTargetData::QGles2RenderTargetData(QRhiImplementation *a0)
extern "C" Q_DECL_EXPORT
QGles2RenderTargetData *ritual_ZN22QGles2RenderTargetDataC1EP18QRhiImplementation(
    QRhiImplementation *a0) {
  return new QGles2RenderTargetData(a0);
}

//  bool QGles2RenderTargetData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGles2RenderTargetData7isValidEv(
    const QGles2RenderTargetData *self) {
  return self->isValid();
}

//  QGles2RenderTargetData::~QGles2RenderTargetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGles2RenderTargetDataD1Ev(QGles2RenderTargetData *self) {
  delete self;
}
