//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QDBusConnectionPrivate::ObjectTreeNode::ObjectTreeNode()
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate::ObjectTreeNode *ritual_ZN22QDBusConnectionPrivate14ObjectTreeNodeC1Ev() {
  return new QDBusConnectionPrivate::ObjectTreeNode();
}

//  QDBusConnectionPrivate::ObjectTreeNode::ObjectTreeNode(const QString &n)
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate::ObjectTreeNode *ritual_ZN22QDBusConnectionPrivate14ObjectTreeNodeC1ERK7QString(
    const QString *n) {
  return new QDBusConnectionPrivate::ObjectTreeNode(*n);
}

//  bool QDBusConnectionPrivate::ObjectTreeNode::operator<(const QString
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDBusConnectionPrivate14ObjectTreeNodeltERK7QString(
    const QDBusConnectionPrivate::ObjectTreeNode *self,
    const QString *other) {
  return self->operator<(*other);
}

//  bool QDBusConnectionPrivate::ObjectTreeNode::operator<(QStringView other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDBusConnectionPrivate14ObjectTreeNodeltE11QStringView(
    const QDBusConnectionPrivate::ObjectTreeNode *self,
    const QString *other) {
  return self->operator<(QStringView(*other));
}

//  bool QDBusConnectionPrivate::ObjectTreeNode::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDBusConnectionPrivate14ObjectTreeNode8isActiveEv(
    const QDBusConnectionPrivate::ObjectTreeNode *self) {
  return self->isActive();
}

//  QDBusConnectionPrivate::ObjectTreeNode::~ObjectTreeNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate14ObjectTreeNodeD1Ev(
    QDBusConnectionPrivate::ObjectTreeNode *self) {
  delete self;
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
