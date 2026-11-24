//  Written by dev_tooling.RitualGenerator from the records of
//  QtUiPlugin/customwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtUiPlugin/customwidget.h>
#include <QtCore/qlist.h>

//  QDesignerCustomWidgetCollectionInterface::~QDesignerCustomWidgetCollectio
//      nInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QDesignerCustomWidgetCollectionInterfaceD1Ev(
    QDesignerCustomWidgetCollectionInterface *self) {
  delete self;
}

//  QList<QDesignerCustomWidgetInterface *>
//      QDesignerCustomWidgetCollectionInterface::customWidgets() const
extern "C" Q_DECL_EXPORT
QList<QDesignerCustomWidgetInterface *> *ritual_ZNK40QDesignerCustomWidgetCollectionInterface13customWidgetsEv(
    const QDesignerCustomWidgetCollectionInterface *self) {
  return new QList<QDesignerCustomWidgetInterface *>(self->customWidgets());
}
