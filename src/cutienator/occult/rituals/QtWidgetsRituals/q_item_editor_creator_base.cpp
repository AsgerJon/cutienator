//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qitemeditorfactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qitemeditorfactory.h>
#include <QtCore/qbytearray.h>

//  QItemEditorCreatorBase::~QItemEditorCreatorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QItemEditorCreatorBaseD1Ev(QItemEditorCreatorBase *self) {
  delete self;
}

//  QWidget *QItemEditorCreatorBase::createWidget(QWidget *parent) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK22QItemEditorCreatorBase12createWidgetEP7QWidget(
    const QItemEditorCreatorBase *self,
    QWidget *parent) {
  return self->createWidget(parent);
}

//  QByteArray QItemEditorCreatorBase::valuePropertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QItemEditorCreatorBase17valuePropertyNameEv(
    const QItemEditorCreatorBase *self) {
  return new QByteArray(self->valuePropertyName());
}
