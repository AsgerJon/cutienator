//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <memory>
#include <QtCore/QString>

//  QAbstractFileEngineHandler::~QAbstractFileEngineHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractFileEngineHandlerD1Ev(
    QAbstractFileEngineHandler *self) {
  delete self;
}

//  std::unique_ptr<QAbstractFileEngine>
//      QAbstractFileEngineHandler::create(const QString &fileName) const
extern "C" Q_DECL_EXPORT
std::unique_ptr<QAbstractFileEngine> *ritual_ZNK26QAbstractFileEngineHandler6createERK7QString(
    const QAbstractFileEngineHandler *self,
    const QString *fileName) {
  return new std::unique_ptr<QAbstractFileEngine>(self->create(*fileName));
}

//  a std::unique_ptr<QAbstractFileEngine> a ritual of
//      QAbstractFileEngineHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractFileEngineHandler__std_unique_ptr_QAbstractFileEngine(
    std::unique_ptr<QAbstractFileEngine> *self) {
  delete self;
}
