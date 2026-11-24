//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusmenutypes_p.h"
#include <QDBusConnection>
#include <QDBusMetaType>
#include <QImage>
#include <QIcon>
#include <QImage>
#include <QPixmap>
#include <QDebug>
#include <QtEndian>
#include <QBuffer>
#if QT_CONFIG(shortcut)
#  include <private/qkeysequence_p.h>
#endif
#include <qpa/qplatformmenu.h>
#include "qdbusplatformmenu_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 203, as _ZN13QDBusMenuItem15convertMnemonicERK7QString
inline QString QDBusMenuItem::convertMnemonic(const QString &label)
{
    // convert only the first occurrence of ampersand which is not at the end
    // dbusmenu uses underscore instead of ampersand
    int idx = label.indexOf(u'&');
    if (idx < 0 || idx == label.size() - 1)
        return label;
    QString ret(label);
    ret[idx] = u'_';
    return ret;
}
//  -----------------------------------------------------------------------

//  QDBusMenuItem::QDBusMenuItem()
extern "C" Q_DECL_EXPORT
QDBusMenuItem *ritual_ZN13QDBusMenuItemC1Ev() {
  return new QDBusMenuItem();
}

//  QString QDBusMenuItem::convertMnemonic(const QString &label)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QDBusMenuItem15convertMnemonicERK7QString(
    const QString *label) {
  return new QString(QDBusMenuItem::convertMnemonic(*label));
}

//  QDBusMenuItem::~QDBusMenuItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusMenuItemD1Ev(QDBusMenuItem *self) {
  delete self;
}

//  QList<QDBusMenuItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QDBusMenuItem> *ritual_list_make_QDBusMenuItem() {
  return new QList<QDBusMenuItem>();
}

//  void QList<QDBusMenuItem>::append(const QDBusMenuItem &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDBusMenuItem(
    QList<QDBusMenuItem> *self,
    const QDBusMenuItem *element) {
  self->append(*element);
}

//  qsizetype QList<QDBusMenuItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDBusMenuItem(const QList<QDBusMenuItem> *self) {
  return self->size();
}

//  const QDBusMenuItem &QList<QDBusMenuItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDBusMenuItem *ritual_list_at_QDBusMenuItem(
    const QList<QDBusMenuItem> *self,
    long long index) {
  return new QDBusMenuItem(self->at(index));
}

//  QList<QDBusMenuItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDBusMenuItem(QList<QDBusMenuItem> *self) {
  delete self;
}
