//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>

//  QAccessibleImageInterface::~QAccessibleImageInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleImageInterfaceD1Ev(
    QAccessibleImageInterface *self) {
  delete self;
}

//  QString QAccessibleImageInterface::imageDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAccessibleImageInterface16imageDescriptionEv(
    const QAccessibleImageInterface *self) {
  return new QString(self->imageDescription());
}

//  QSize QAccessibleImageInterface::imageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QAccessibleImageInterface9imageSizeEv(
    const QAccessibleImageInterface *self) {
  return new QSize(self->imageSize());
}

//  QPoint QAccessibleImageInterface::imagePosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK25QAccessibleImageInterface13imagePositionEv(
    const QAccessibleImageInterface *self) {
  return new QPoint(self->imagePosition());
}
