//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleHyperlinkInterface::~QAccessibleHyperlinkInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleHyperlinkInterfaceD1Ev(
    QAccessibleHyperlinkInterface *self) {
  delete self;
}

//  QString QAccessibleHyperlinkInterface::anchor() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QAccessibleHyperlinkInterface6anchorEv(
    const QAccessibleHyperlinkInterface *self) {
  return new QString(self->anchor());
}

//  QString QAccessibleHyperlinkInterface::anchorTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QAccessibleHyperlinkInterface12anchorTargetEv(
    const QAccessibleHyperlinkInterface *self) {
  return new QString(self->anchorTarget());
}

//  int QAccessibleHyperlinkInterface::startIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleHyperlinkInterface10startIndexEv(
    const QAccessibleHyperlinkInterface *self) {
  return self->startIndex();
}

//  int QAccessibleHyperlinkInterface::endIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleHyperlinkInterface8endIndexEv(
    const QAccessibleHyperlinkInterface *self) {
  return self->endIndex();
}

//  bool QAccessibleHyperlinkInterface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleHyperlinkInterface7isValidEv(
    const QAccessibleHyperlinkInterface *self) {
  return self->isValid();
}
