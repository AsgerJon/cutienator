//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaqualifiedname.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaqualifiedname.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QOpcUaQualifiedName::QOpcUaQualifiedName()
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZN19QOpcUaQualifiedNameC1Ev() {
  return new QOpcUaQualifiedName();
}

//  QOpcUaQualifiedName::QOpcUaQualifiedName(const QOpcUaQualifiedName &a0)
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZN19QOpcUaQualifiedNameC1ERKS_(
    const QOpcUaQualifiedName *a0) {
  return new QOpcUaQualifiedName(*a0);
}

//  QOpcUaQualifiedName::QOpcUaQualifiedName(quint16 namespaceIndex, const
//      QString &name)
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZN19QOpcUaQualifiedNameC1EtRK7QString(
    quint16 namespaceIndex,
    const QString *name) {
  return new QOpcUaQualifiedName(namespaceIndex, *name);
}

//  bool QOpcUaQualifiedName::operator==(const QOpcUaQualifiedName &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaQualifiedNameeqERKS_(
    const QOpcUaQualifiedName *self,
    const QOpcUaQualifiedName *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaQualifiedName::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QOpcUaQualifiedNamecv8QVariantEv(
    const QOpcUaQualifiedName *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaQualifiedName::~QOpcUaQualifiedName()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaQualifiedNameD1Ev(QOpcUaQualifiedName *self) {
  delete self;
}

//  QString QOpcUaQualifiedName::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QOpcUaQualifiedName4nameEv(
    const QOpcUaQualifiedName *self) {
  return new QString(self->name());
}

//  void QOpcUaQualifiedName::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaQualifiedName7setNameERK7QString(
    QOpcUaQualifiedName *self,
    const QString *name) {
  self->setName(*name);
}

//  quint16 QOpcUaQualifiedName::namespaceIndex() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK19QOpcUaQualifiedName14namespaceIndexEv(
    const QOpcUaQualifiedName *self) {
  return self->namespaceIndex();
}

//  void QOpcUaQualifiedName::setNamespaceIndex(quint16 namespaceIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaQualifiedName17setNamespaceIndexEt(
    QOpcUaQualifiedName *self,
    quint16 namespaceIndex) {
  self->setNamespaceIndex(namespaceIndex);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QOpcUaQualifiedName &qn)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QOpcUaQualifiedName(
    const QDebug *debug,
    const QOpcUaQualifiedName *qn) {
  return new QDebug(operator<<(*debug, *qn));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QOpcUaQualifiedName>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaQualifiedName> *ritual_list_make_QOpcUaQualifiedName() {
  return new QList<QOpcUaQualifiedName>();
}

//  void QList<QOpcUaQualifiedName>::append(const QOpcUaQualifiedName &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaQualifiedName(
    QList<QOpcUaQualifiedName> *self,
    const QOpcUaQualifiedName *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaQualifiedName>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaQualifiedName(
    const QList<QOpcUaQualifiedName> *self) {
  return self->size();
}

//  const QOpcUaQualifiedName &QList<QOpcUaQualifiedName>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_list_at_QOpcUaQualifiedName(
    const QList<QOpcUaQualifiedName> *self,
    long long index) {
  return new QOpcUaQualifiedName(self->at(index));
}

//  QList<QOpcUaQualifiedName>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaQualifiedName(QList<QOpcUaQualifiedName> *self) {
  delete self;
}
