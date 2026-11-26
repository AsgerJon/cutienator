//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomtheme_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcustomtheme_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 62, as _ZNK21QQStyleKitCustomTheme4nameEv
inline QString QQStyleKitCustomTheme::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 75, as _ZNK21QQStyleKitCustomTheme5themeEv
inline QQmlComponent *QQStyleKitCustomTheme::theme() const
{
    return m_theme;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitCustomTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQStyleKitCustomTheme10metaObjectEv(
    const QQStyleKitCustomTheme *self) {
  return self->metaObject();
}

//  void *QQStyleKitCustomTheme::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQStyleKitCustomTheme11qt_metacastEPKc(
    QQStyleKitCustomTheme *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitCustomTheme::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQStyleKitCustomTheme11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitCustomTheme *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitCustomTheme::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQStyleKitCustomTheme4nameEv(
    const QQStyleKitCustomTheme *self) {
  return new QString(self->name());
}

//  QQmlComponent *QQStyleKitCustomTheme::theme() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK21QQStyleKitCustomTheme5themeEv(
    const QQStyleKitCustomTheme *self) {
  return self->theme();
}

//  void QQStyleKitCustomTheme::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQStyleKitCustomTheme11nameChangedEv(
    QQStyleKitCustomTheme *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitCustomTheme")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "nameChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "nameChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitCustomTheme::themeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQStyleKitCustomTheme12themeChangedEv(
    QQStyleKitCustomTheme *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitCustomTheme")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "themeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "themeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QList<QQStyleKitCustomTheme *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQStyleKitCustomTheme *> *ritual_list_make_QQStyleKitCustomTheme_ptr() {
  return new QList<QQStyleKitCustomTheme *>();
}

//  void QList<QQStyleKitCustomTheme *>::append(const QQStyleKitCustomTheme *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQStyleKitCustomTheme_ptr(
    QList<QQStyleKitCustomTheme *> *self,
    QQStyleKitCustomTheme *element) {
  self->append(element);
}

//  qsizetype QList<QQStyleKitCustomTheme *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQStyleKitCustomTheme_ptr(
    const QList<QQStyleKitCustomTheme *> *self) {
  return self->size();
}

//  const QQStyleKitCustomTheme * &QList<QQStyleKitCustomTheme
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQStyleKitCustomTheme *ritual_list_at_QQStyleKitCustomTheme_ptr(
    const QList<QQStyleKitCustomTheme *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQStyleKitCustomTheme *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQStyleKitCustomTheme_ptr(
    QList<QQStyleKitCustomTheme *> *self) {
  delete self;
}
