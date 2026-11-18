//  Apache-2.0 license
//  Copyright (c) 2026 Asger Jon Vistisen
//
//  q_object.cpp: QObject's own functions, each under a plain name.
//  The name is always the class, an underscore, and Qt's function name.
//  The first thing each function takes is the address of the object.
//  The comment above each function is Qt's own declaration.
#include <QtCore/QByteArray>
#include <QtCore/QObject>
#include <QtCore/QString>

//  Qt: QObject(QObject *parent = nullptr)
extern "C" QObject *QObject_new(QObject *parent) {
  return new QObject(parent);
}

//  Qt: ~QObject()
extern "C" void QObject_delete(QObject *self) {
  delete self;
}

//  Qt: QObject *parent() const
extern "C" QObject *QObject_parent(QObject *self) {
  return self->parent();
}

//  Qt: void setParent(QObject *parent)
extern "C" void QObject_setParent(QObject *self, QObject *parent) {
  self->setParent(parent);
}

//  Qt: bool isWidgetType() const
extern "C" bool QObject_isWidgetType(QObject *self) {
  return self->isWidgetType();
}

//  Qt: bool signalsBlocked() const
extern "C" bool QObject_signalsBlocked(QObject *self) {
  return self->signalsBlocked();
}

//  Qt: bool blockSignals(bool block)
extern "C" bool QObject_blockSignals(QObject *self, bool block) {
  return self->blockSignals(block);
}

//  Qt: bool inherits(const char *className) const
extern "C" bool QObject_inherits(QObject *self, const char *className) {
  return self->inherits(className);
}

//  Qt: void deleteLater()
extern "C" void QObject_deleteLater(QObject *self) {
  self->deleteLater();
}

//  Qt: void setObjectName(const QString &name)
//  Text goes in as UTF-8 bytes.
extern "C" void QObject_setObjectName(QObject *self, const char *name) {
  self->setObjectName(QString::fromUtf8(name));
}

//  Qt: QString objectName() const
//  Text comes back as the address of a new QByteArray holding UTF-8,
//  which the caller reads and then deletes with QByteArray_delete.
extern "C" QByteArray *QObject_objectName(QObject *self) {
  return new QByteArray(self->objectName().toUtf8());
}
