//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qquaternion.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_QUATERNION)
#include <QtGui/qquaternion.h>

//  QQuaternion::Axes::~Axes()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion4AxesD1Ev(QQuaternion::Axes *self) {
  delete self;
}

#endif  // !defined(QT_NO_QUATERNION)
