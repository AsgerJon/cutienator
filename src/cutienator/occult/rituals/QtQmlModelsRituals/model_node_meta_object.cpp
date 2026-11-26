//  Written by hand on 2026-11-25 from
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name (no export macro
//  on the class line): only its inline function and its virtual
//  functions are called, through the object. Of the two declarations of
//  'toDynamicMetaObject' the one Qt 6 builds is written (the other
//  stands under QT_VERSION 7).
//  Not written: the constructor; 'get', 'updateValues' and
//  'emitDirectNotifies' (defined in Qt's library under no export);
//  'updateValues(QList)' (a QList).
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h>

//  ModelNodeMetaObject::~ModelNodeMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19ModelNodeMetaObjectD1Ev(ModelNodeMetaObject *self) {
  delete self;
}

//  QMetaObject *ModelNodeMetaObject::toDynamicMetaObject(QObject *object)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN19ModelNodeMetaObject18toDynamicMetaObjectEP7QObject(
    ModelNodeMetaObject *self,
    QObject *object) {
  return self->toDynamicMetaObject(object);
}

//  bool ModelNodeMetaObject::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19ModelNodeMetaObject11initializedEv(
    const ModelNodeMetaObject *self) {
  return self->initialized();
}

//  void ModelNodeMetaObject::propertyWritten(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19ModelNodeMetaObject15propertyWrittenEi(
    ModelNodeMetaObject *self,
    int index) {
  self->propertyWritten(index);
}

#endif  // QT_CONFIG(qml_list_model)
