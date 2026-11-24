//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquicktableviewdelegate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktableviewdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickTableViewDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTableViewDelegate : QQuickTableViewDelegate {
  using QQuickTableViewDelegate::defaultFont;
  using QQuickTableViewDelegate::mousePressEvent;
};

//  const QMetaObject *QQuickTableViewDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickTableViewDelegate10metaObjectEv(
    const QQuickTableViewDelegate *self) {
  return self->metaObject();
}

//  QString QQuickTableViewDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickTableViewDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTableViewDelegate::tr(s, c, n));
}

//  QQuickTableViewDelegate::QQuickTableViewDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTableViewDelegate *ritual_ZN23QQuickTableViewDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTableViewDelegate(parent);
}

//  bool QQuickTableViewDelegate::current() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickTableViewDelegate7currentEv(
    const QQuickTableViewDelegate *self) {
  return self->current();
}

//  void QQuickTableViewDelegate::setCurrent(bool current)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewDelegate10setCurrentEb(
    QQuickTableViewDelegate *self,
    bool current) {
  self->setCurrent(current);
}

//  bool QQuickTableViewDelegate::selected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickTableViewDelegate8selectedEv(
    const QQuickTableViewDelegate *self) {
  return self->selected();
}

//  void QQuickTableViewDelegate::setSelected(bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewDelegate11setSelectedEb(
    QQuickTableViewDelegate *self,
    bool selected) {
  self->setSelected(selected);
}

//  bool QQuickTableViewDelegate::editing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickTableViewDelegate7editingEv(
    const QQuickTableViewDelegate *self) {
  return self->editing();
}

//  void QQuickTableViewDelegate::setEditing(bool editing)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewDelegate10setEditingEb(
    QQuickTableViewDelegate *self,
    bool editing) {
  self->setEditing(editing);
}

//  QQuickTableView *QQuickTableViewDelegate::tableView() const
extern "C" Q_DECL_EXPORT
QQuickTableView *ritual_ZNK23QQuickTableViewDelegate9tableViewEv(
    const QQuickTableViewDelegate *self) {
  return self->tableView();
}

//  void QQuickTableViewDelegate::setTableView(QQuickTableView *tableView)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewDelegate12setTableViewEP15QQuickTableView(
    QQuickTableViewDelegate *self,
    QQuickTableView *tableView) {
  self->setTableView(tableView);
}

//  QFont QQuickTableViewDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QQuickTableViewDelegate11defaultFontEv(
    const QQuickTableViewDelegate *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickTableViewDelegate::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewDelegate15mousePressEventEP11QMouseEvent(
    QQuickTableViewDelegate *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  QQuickTableViewDelegatePrivate *QQuickTableViewDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickTableViewDelegatePrivate *ritual_ZN23QQuickTableViewDelegate6d_funcEv(
    QQuickTableViewDelegate *self) {
  return self->d_func();
}

//  const QQuickTableViewDelegatePrivate *QQuickTableViewDelegate::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickTableViewDelegatePrivate *ritual_ZNK23QQuickTableViewDelegate6d_funcEv(
    const QQuickTableViewDelegate *self) {
  return self->d_func();
}

//  QFont QQuickTableViewDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK23QQuickTableViewDelegate11defaultFontEv(
    const QQuickTableViewDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickTableViewDelegate *>(self)->OwnQQuickTableViewDelegate::defaultFont());
}

//  void QQuickTableViewDelegate::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickTableViewDelegate15mousePressEventEP11QMouseEvent(
    QQuickTableViewDelegate *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTableViewDelegate *>(self)->OwnQQuickTableViewDelegate::mousePressEvent(
      event);
}

#endif  // QT_CONFIG(quick_tableview)
