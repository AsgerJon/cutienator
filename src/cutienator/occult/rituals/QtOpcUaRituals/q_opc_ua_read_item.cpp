//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuareaditem.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuareaditem.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QOpcUaReadItem::QOpcUaReadItem()
extern "C" Q_DECL_EXPORT
QOpcUaReadItem *ritual_ZN14QOpcUaReadItemC1Ev() {
  return new QOpcUaReadItem();
}

//  QOpcUaReadItem::QOpcUaReadItem(const QOpcUaReadItem &other)
extern "C" Q_DECL_EXPORT
QOpcUaReadItem *ritual_ZN14QOpcUaReadItemC1ERKS_(
    const QOpcUaReadItem *other) {
  return new QOpcUaReadItem(*other);
}

//  QOpcUaReadItem::QOpcUaReadItem(const QString &nodeId,
//      QOpcUa::NodeAttribute attr, const QString &indexRange)
extern "C" Q_DECL_EXPORT
QOpcUaReadItem *ritual_ZN14QOpcUaReadItemC1ERK7QStringN6QOpcUa13NodeAttributeES2_(
    const QString *nodeId,
    QOpcUa::NodeAttribute attr,
    const QString *indexRange) {
  return new QOpcUaReadItem(*nodeId, attr, *indexRange);
}

//  QOpcUaReadItem::~QOpcUaReadItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaReadItemD1Ev(QOpcUaReadItem *self) {
  delete self;
}

//  QString QOpcUaReadItem::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOpcUaReadItem6nodeIdEv(const QOpcUaReadItem *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaReadItem::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaReadItem9setNodeIdERK7QString(
    QOpcUaReadItem *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  QOpcUa::NodeAttribute QOpcUaReadItem::attribute() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeAttribute ritual_ZNK14QOpcUaReadItem9attributeEv(
    const QOpcUaReadItem *self) {
  return self->attribute();
}

//  void QOpcUaReadItem::setAttribute(QOpcUa::NodeAttribute attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaReadItem12setAttributeEN6QOpcUa13NodeAttributeE(
    QOpcUaReadItem *self,
    QOpcUa::NodeAttribute attribute) {
  self->setAttribute(attribute);
}

//  QString QOpcUaReadItem::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOpcUaReadItem10indexRangeEv(
    const QOpcUaReadItem *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaReadItem::setIndexRange(const QString &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaReadItem13setIndexRangeERK7QString(
    QOpcUaReadItem *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}

//  bool operator==(const QOpcUaReadItem &lhs, const QOpcUaReadItem &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QOpcUaReadItemS1_(
    const QOpcUaReadItem *lhs,
    const QOpcUaReadItem *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaReadItem &lhs, const QOpcUaReadItem &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QOpcUaReadItemS1_(
    const QOpcUaReadItem *lhs,
    const QOpcUaReadItem *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaReadItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaReadItem> *ritual_list_make_QOpcUaReadItem() {
  return new QList<QOpcUaReadItem>();
}

//  void QList<QOpcUaReadItem>::append(const QOpcUaReadItem &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaReadItem(
    QList<QOpcUaReadItem> *self,
    const QOpcUaReadItem *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaReadItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaReadItem(
    const QList<QOpcUaReadItem> *self) {
  return self->size();
}

//  const QOpcUaReadItem &QList<QOpcUaReadItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaReadItem *ritual_list_at_QOpcUaReadItem(
    const QList<QOpcUaReadItem> *self,
    long long index) {
  return new QOpcUaReadItem(self->at(index));
}

//  QList<QOpcUaReadItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaReadItem(QList<QOpcUaReadItem> *self) {
  delete self;
}
