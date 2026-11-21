//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qitemeditorfactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qitemeditorfactory.h>
#include <QtCore/qbytearray.h>

//  QItemEditorFactory::QItemEditorFactory()
extern "C" Q_DECL_EXPORT
QItemEditorFactory *ritual_ZN18QItemEditorFactoryC1Ev() {
  return new QItemEditorFactory();
}

//  QItemEditorFactory::~QItemEditorFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemEditorFactoryD1Ev(QItemEditorFactory *self) {
  delete self;
}

//  QWidget *QItemEditorFactory::createEditor(int userType, QWidget *parent)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18QItemEditorFactory12createEditorEiP7QWidget(
    const QItemEditorFactory *self,
    int userType,
    QWidget *parent) {
  return self->createEditor(userType, parent);
}

//  QByteArray QItemEditorFactory::valuePropertyName(int userType) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QItemEditorFactory17valuePropertyNameEi(
    const QItemEditorFactory *self,
    int userType) {
  return new QByteArray(self->valuePropertyName(userType));
}

//  void QItemEditorFactory::registerEditor(int userType,
//      QItemEditorCreatorBase *creator)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemEditorFactory14registerEditorEiP22QItemEditorCreatorBase(
    QItemEditorFactory *self,
    int userType,
    QItemEditorCreatorBase *creator) {
  self->registerEditor(userType, creator);
}

//  const QItemEditorFactory *QItemEditorFactory::defaultFactory()
extern "C" Q_DECL_EXPORT
const QItemEditorFactory *ritual_ZN18QItemEditorFactory14defaultFactoryEv() {
  return QItemEditorFactory::defaultFactory();
}

//  void QItemEditorFactory::setDefaultFactory(QItemEditorFactory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemEditorFactory17setDefaultFactoryEPS_(
    QItemEditorFactory *factory) {
  QItemEditorFactory::setDefaultFactory(factory);
}
