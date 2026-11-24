//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextdocumentfragment.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicktextcontrol_p.h"
#include "qquicktextcontrol_p_p.h"
#ifndef QT_NO_TEXTCONTROL
#include <qcoreapplication.h>
#include <qfont.h>
#include <qfontmetrics.h>
#include <qevent.h>
#include <qdebug.h>
#include <qclipboard.h>
#include <qtimer.h>
#include <qinputmethod.h>
#include "private/qtextdocumentlayout_p.h"
#include "private/qabstracttextdocumentlayout_p.h"
#include "qtextdocument.h"
#include "private/qtextdocument_p.h"
#include "qtextlist.h"
#include "qtextdocumentwriter.h"
#include "private/qtextcursor_p.h"
#include <QtCore/qloggingcategory.h>
#include <qtextformat.h>
#include <qtransform.h>
#include <qdatetime.h>
#include <qbuffer.h>
#include <qguiapplication.h>
#include <limits.h>
#include <qtexttable.h>
#include <qvariant.h>
#include <qurl.h>
#include <qstylehints.h>
#include <qmetaobject.h>
#include <private/qqmlglobal_p.h>
#include <private/qquickdeliveryagent_p_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1902, as _ZNK22QQuickTextEditMimeData7formatsEv
#if !defined(QT_NO_TEXTCONTROL)
inline QStringList QQuickTextEditMimeData::formats() const
{
    if (!fragment.isEmpty())
        return QStringList() << QString::fromLatin1("text/plain") << QString::fromLatin1("text/html")
#if QT_CONFIG(textodfwriter)
            << QString::fromLatin1("application/vnd.oasis.opendocument.text")
#endif
        ;
    else
        return QMimeData::formats();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1914, as _ZNK22QQuickTextEditMimeData12retrieveDataERK7QString9QMetaType
#if !defined(QT_NO_TEXTCONTROL)
inline QVariant QQuickTextEditMimeData::retrieveData(const QString &mimeType, QMetaType type) const
{
    if (!fragment.isEmpty())
        setup();
    return QMimeData::retrieveData(mimeType, type);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1921, as _ZNK22QQuickTextEditMimeData5setupEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextEditMimeData::setup() const
{
    QQuickTextEditMimeData *that = const_cast<QQuickTextEditMimeData *>(this);
#if QT_CONFIG(texthtmlparser)
    that->setData(QLatin1String("text/html"), fragment.toHtml().toUtf8());
#endif
#if QT_CONFIG(textodfwriter)
    {
        QBuffer buffer;
        QTextDocumentWriter writer(&buffer, "ODF");
        writer.write(fragment);
        buffer.close();
        that->setData(QLatin1String("application/vnd.oasis.opendocument.text"), buffer.data());
    }
#endif
    that->setText(fragment.toPlainText());
    fragment = QTextDocumentFragment();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickTextEditMimeData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTextEditMimeData : QQuickTextEditMimeData {
  using QQuickTextEditMimeData::retrieveData;
};

#if !defined(QT_NO_TEXTCONTROL)
//  QQuickTextEditMimeData::QQuickTextEditMimeData(const
//      QTextDocumentFragment &aFragment)
extern "C" Q_DECL_EXPORT
QQuickTextEditMimeData *ritual_ZN22QQuickTextEditMimeDataC1ERK21QTextDocumentFragment(
    const QTextDocumentFragment *aFragment) {
  return new QQuickTextEditMimeData(*aFragment);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  QStringList QQuickTextEditMimeData::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QQuickTextEditMimeData7formatsEv(
    const QQuickTextEditMimeData *self) {
  return new QList<QString>(self->formats());
}

//  QVariant QQuickTextEditMimeData::retrieveData(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QQuickTextEditMimeData12retrieveDataERK7QString9QMetaType(
    const QQuickTextEditMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(self->retrieveData(*mimeType, *type));
}

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextEditMimeData::setup() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickTextEditMimeData5setupEv(
    const QQuickTextEditMimeData *self) {
  self->setup();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QVariant QQuickTextEditMimeData::retrieveData(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QQuickTextEditMimeData12retrieveDataERK7QString9QMetaType(
    const QQuickTextEditMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(
      static_cast<const OwnQQuickTextEditMimeData *>(self)->OwnQQuickTextEditMimeData::retrieveData(
          *mimeType,
          *type));
}
#endif  // !defined(QT_NO_TEXTCONTROL)
