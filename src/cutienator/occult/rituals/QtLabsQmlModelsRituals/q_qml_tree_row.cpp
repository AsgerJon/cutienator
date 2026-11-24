//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltreerow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/qtlabsqmlmodelsexports.h>
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/QtLabsQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltreerow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsQmlModels/private/qqmltreerow_p.h>
#include <QtCore/qjsonobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 13, as _ZN11QQmlTreeRowC1EPS_
inline QQmlTreeRow::QQmlTreeRow(QQmlTreeRow *parentItem)
    : m_parent(parentItem)
{

}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 19, as _ZN11QQmlTreeRowC1ERK8QVariantPS_
inline QQmlTreeRow::QQmlTreeRow(const QVariant &data, QQmlTreeRow *parentItem)
    : m_parent(parentItem)
{
    QVariantMap variantMap = data.toMap();
    unpackVariantMap(variantMap);
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 26, as _ZN11QQmlTreeRowC1ERK4QMapI7QString8QVariantEPS_
inline QQmlTreeRow::QQmlTreeRow(const QVariantMap &data, QQmlTreeRow *parentItem)
    : m_parent(parentItem)
{
    unpackVariantMap(data);
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 32, as _ZN11QQmlTreeRow8addChildEPS_
inline void QQmlTreeRow::addChild(QQmlTreeRow *child)
{
    m_children.push_back(std::unique_ptr<QQmlTreeRow>(child));
    child->setParent(this);
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 112, as _ZNK11QQmlTreeRow11subTreeSizeEv
inline int QQmlTreeRow::subTreeSize() const
{
    int size = 1;

    for (const auto &child : m_children)
        size += child->subTreeSize();

    return size;
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 65, as _ZN11QQmlTreeRow13removeChildAtEi
inline void QQmlTreeRow::removeChildAt(int i)
{
    m_children.erase(std::next(m_children.begin(), i));
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 78, as _ZN11QQmlTreeRow7setDataERK8QVariant
inline void QQmlTreeRow::setData(const QVariant &data)
{
    dataMap.clear();
    const QVariantMap variantMap = data.toJsonObject().toVariantMap();
    unpackVariantMap(variantMap);
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 85, as _ZN11QQmlTreeRow7setDataERK4QMapI7QString8QVariantE
inline void QQmlTreeRow::setData(const QVariantMap &data)
{
    dataMap.clear();
    unpackVariantMap(data);
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 91, as _ZN11QQmlTreeRow8setFieldERK7QStringRK8QVariant
inline void QQmlTreeRow::setField(const QString &key, const QVariant &value)
{
    if (dataMap.contains(key))
        dataMap[key] = value;
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 97, as _ZNK11QQmlTreeRow9toVariantEv
inline QVariant QQmlTreeRow::toVariant() const
{
    QVariantMap variantMap(dataMap);

    if (!m_children.empty()) {
        QVariantList children;
        for (const auto &child : m_children)
            children.append(child->toVariant());

        variantMap[ROWS_PROPERTY_NAME] = children;
    }

    return variantMap;
}

//  from ../qtdeclarative/src/labs/models/qqmltreerow.cpp, line 44, as _ZN11QQmlTreeRow16unpackVariantMapERK4QMapI7QString8QVariantE
inline void QQmlTreeRow::unpackVariantMap(const QVariantMap &variantMap)
{
    for (auto it = variantMap.begin(); it != variantMap.end(); ++it) {
        const QString& key = it.key();
        const QVariant& value = it.value();

        if ((value.typeId() == QMetaType::Type::QVariantList) && (key == ROWS_PROPERTY_NAME)) {
            const QList<QVariant> variantList = value.toList();
            for (const QVariant &rowAsVariant : variantList)
                m_children.push_back(std::make_unique<QQmlTreeRow>(rowAsVariant, this));
        } else {
            dataMap.insert(key, value);
        }
    }
}
//  -----------------------------------------------------------------------

//  QQmlTreeRow::QQmlTreeRow(QQmlTreeRow *parentItem)
extern "C" Q_DECL_EXPORT
QQmlTreeRow *ritual_ZN11QQmlTreeRowC1EPS_(QQmlTreeRow *parentItem) {
  return new QQmlTreeRow(parentItem);
}

//  QQmlTreeRow::QQmlTreeRow(const QVariant &data, QQmlTreeRow *parentItem)
extern "C" Q_DECL_EXPORT
QQmlTreeRow *ritual_ZN11QQmlTreeRowC1ERK8QVariantPS_(
    const QVariant *data,
    QQmlTreeRow *parentItem) {
  return new QQmlTreeRow(*data, parentItem);
}

//  QQmlTreeRow::QQmlTreeRow(const QVariantMap &data, QQmlTreeRow
//      *parentItem)
extern "C" Q_DECL_EXPORT
QQmlTreeRow *ritual_ZN11QQmlTreeRowC1ERK4QMapI7QString8QVariantEPS_(
    const QMap<QString, QVariant> *data,
    QQmlTreeRow *parentItem) {
  return new QQmlTreeRow(*data, parentItem);
}

//  QQmlTreeRow *QQmlTreeRow::parent() const
extern "C" Q_DECL_EXPORT
QQmlTreeRow *ritual_ZNK11QQmlTreeRow6parentEv(const QQmlTreeRow *self) {
  return self->parent();
}

//  void QQmlTreeRow::setParent(QQmlTreeRow *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow9setParentEPS_(
    QQmlTreeRow *self,
    QQmlTreeRow *parent) {
  self->setParent(parent);
}

//  const QQmlTreeRow *QQmlTreeRow::getRow(int i) const
extern "C" Q_DECL_EXPORT
const QQmlTreeRow *ritual_ZNK11QQmlTreeRow6getRowEi(
    const QQmlTreeRow *self,
    int i) {
  return self->getRow(i);
}

//  void QQmlTreeRow::addChild(QQmlTreeRow *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow8addChildEPS_(
    QQmlTreeRow *self,
    QQmlTreeRow *child) {
  self->addChild(child);
}

//  int QQmlTreeRow::subTreeSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QQmlTreeRow11subTreeSizeEv(const QQmlTreeRow *self) {
  return self->subTreeSize();
}

//  QVariantMap QQmlTreeRow::data() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK11QQmlTreeRow4dataEv(
    const QQmlTreeRow *self) {
  return new QMap<QString, QVariant>(self->data());
}

//  QVariant QQmlTreeRow::data(const QString &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QQmlTreeRow4dataERK7QString(
    const QQmlTreeRow *self,
    const QString *key) {
  return new QVariant(self->data(*key));
}

//  void QQmlTreeRow::removeChildAt(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow13removeChildAtEi(QQmlTreeRow *self, int i) {
  self->removeChildAt(i);
}

//  void QQmlTreeRow::setData(const QVariant &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow7setDataERK8QVariant(
    QQmlTreeRow *self,
    const QVariant *data) {
  self->setData(*data);
}

//  void QQmlTreeRow::setData(const QVariantMap &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow7setDataERK4QMapI7QString8QVariantE(
    QQmlTreeRow *self,
    const QMap<QString, QVariant> *data) {
  self->setData(*data);
}

//  void QQmlTreeRow::setField(const QString &key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow8setFieldERK7QStringRK8QVariant(
    QQmlTreeRow *self,
    const QString *key,
    const QVariant *value) {
  self->setField(*key, *value);
}

//  QVariant QQmlTreeRow::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QQmlTreeRow9toVariantEv(const QQmlTreeRow *self) {
  return new QVariant(self->toVariant());
}

//  void QQmlTreeRow::unpackVariantMap(const QVariantMap &dataMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRow16unpackVariantMapERK4QMapI7QString8QVariantE(
    QQmlTreeRow *self,
    const QMap<QString, QVariant> *dataMap) {
  self->unpackVariantMap(*dataMap);
}

//  QQmlTreeRow::~QQmlTreeRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlTreeRowD1Ev(QQmlTreeRow *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(qml_tree_model)
