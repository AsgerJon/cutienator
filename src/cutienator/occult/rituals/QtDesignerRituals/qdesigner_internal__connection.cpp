//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <cstring>

//  A qdesigner_internal::Connection that Python can take functions over in. Every qdesigner_internal::Connection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_ConnectionCall0)(const void *, int *);
typedef const QRegion * (*Cuteqdesigner_internal_ConnectionCall1)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionCall2)(const void *, QPainter *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionCall3)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionCall4)(const void *, int *);
class Cuteqdesigner_internal_Connection : public qdesigner_internal::Connection {
public:
  using qdesigner_internal::Connection::Connection;
  Cuteqdesigner_internal_Connection(const qdesigner_internal::Connection & other) : qdesigner_internal::Connection(other) {}
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18qdesigner_internal10Connection16updateVisibilityEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal10Connection6regionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal10Connection5paintEP8QPainter")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal10Connection8insertedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal10Connection7removedEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void qdesigner_internal::Connection::updateVisibility()
  void updateVisibility() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionCall0 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::Connection::updateVisibility();
  }

  //  QRegion qdesigner_internal::Connection::region() const
  QRegion region() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionCall1 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionCall1>(taken[1]);
      const QRegion * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return qdesigner_internal::Connection::region();
  }

  //  void qdesigner_internal::Connection::paint(QPainter *p) const
  void paint(QPainter *p) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionCall2 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionCall2>(taken[2]);
      call(this, p, &handled);
      if (handled) return;
    }
    qdesigner_internal::Connection::paint(p);
  }

  //  void qdesigner_internal::Connection::inserted()
  void inserted() override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionCall3 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::Connection::inserted();
  }

  //  void qdesigner_internal::Connection::removed()
  void removed() override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionCall4 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::Connection::removed();
  }
};

//  qdesigner_internal::Connection::Connection(ConnectionEdit *edit)
extern "C" Q_DECL_EXPORT
qdesigner_internal::Connection *ritual_ZN18qdesigner_internal10ConnectionC1EPNS_14ConnectionEditE(
    qdesigner_internal::ConnectionEdit *edit) {
  return new Cuteqdesigner_internal_Connection(edit);
}

//  qdesigner_internal::Connection::Connection(ConnectionEdit *edit, QObject
//      *source, QObject *target)
extern "C" Q_DECL_EXPORT
qdesigner_internal::Connection *ritual_ZN18qdesigner_internal10ConnectionC1EPNS_14ConnectionEditEP7QObjectS4_(
    qdesigner_internal::ConnectionEdit *edit,
    QObject *source,
    QObject *target) {
  return new Cuteqdesigner_internal_Connection(edit, source, target);
}

//  qdesigner_internal::Connection::~Connection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ConnectionD1Ev(
    qdesigner_internal::Connection *self) {
  delete self;
}

//  QObject *qdesigner_internal::Connection::object(EndPoint::Type type)
//      const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18qdesigner_internal10Connection6objectENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return self->object(type);
}

//  QWidget *qdesigner_internal::Connection::widget(EndPoint::Type type)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal10Connection6widgetENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return self->widget(type);
}

//  QPoint qdesigner_internal::Connection::endPointPos(EndPoint::Type type)
//      const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18qdesigner_internal10Connection11endPointPosENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return new QPoint(self->endPointPos(type));
}

//  QRect qdesigner_internal::Connection::endPointRect(EndPoint::Type a0)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal10Connection12endPointRectENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type a0) {
  return new QRect(self->endPointRect(a0));
}

//  void qdesigner_internal::Connection::setEndPoint(EndPoint::Type type,
//      QObject *w, const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection11setEndPointENS_7CETypes8EndPoint4TypeEP7QObjectRK6QPoint(
    qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type,
    QObject *w,
    const QPoint *pos) {
  self->setEndPoint(type, w, *pos);
}

//  bool qdesigner_internal::Connection::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal10Connection9isVisibleEv(
    const qdesigner_internal::Connection *self) {
  return self->isVisible();
}

//  void qdesigner_internal::Connection::updateVisibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection16updateVisibilityEv(
    qdesigner_internal::Connection *self) {
  self->updateVisibility();
}

//  void qdesigner_internal::Connection::setVisible(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection10setVisibleEb(
    qdesigner_internal::Connection *self,
    bool b) {
  self->setVisible(b);
}

//  QRegion qdesigner_internal::Connection::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK18qdesigner_internal10Connection6regionEv(
    const qdesigner_internal::Connection *self) {
  return new QRegion(self->region());
}

//  bool qdesigner_internal::Connection::contains(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal10Connection8containsERK6QPoint(
    const qdesigner_internal::Connection *self,
    const QPoint *pos) {
  return self->contains(*pos);
}

//  void qdesigner_internal::Connection::paint(QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal10Connection5paintEP8QPainter(
    const qdesigner_internal::Connection *self,
    QPainter *p) {
  self->paint(p);
}

//  void qdesigner_internal::Connection::update(bool update_widgets) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal10Connection6updateEb(
    const qdesigner_internal::Connection *self,
    bool update_widgets) {
  self->update(update_widgets);
}

//  void qdesigner_internal::Connection::checkWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection12checkWidgetsEv(
    qdesigner_internal::Connection *self) {
  self->checkWidgets();
}

//  QString qdesigner_internal::Connection::label(EndPoint::Type type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal10Connection5labelENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return new QString(self->label(type));
}

//  void qdesigner_internal::Connection::setLabel(EndPoint::Type type, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection8setLabelENS_7CETypes8EndPoint4TypeERK7QString(
    qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type,
    const QString *text) {
  self->setLabel(type, *text);
}

//  QRect qdesigner_internal::Connection::labelRect(EndPoint::Type type)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal10Connection9labelRectENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return new QRect(self->labelRect(type));
}

//  QPixmap qdesigner_internal::Connection::labelPixmap(EndPoint::Type type)
//      const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK18qdesigner_internal10Connection11labelPixmapENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return new QPixmap(self->labelPixmap(type));
}

//  ConnectionEdit *qdesigner_internal::Connection::edit() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::ConnectionEdit *ritual_ZNK18qdesigner_internal10Connection4editEv(
    const qdesigner_internal::Connection *self) {
  return self->edit();
}

//  void qdesigner_internal::Connection::inserted()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection8insertedEv(
    qdesigner_internal::Connection *self) {
  self->inserted();
}

//  void qdesigner_internal::Connection::removed()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection7removedEv(
    qdesigner_internal::Connection *self) {
  self->removed();
}

//  void qdesigner_internal::Connection::setSource(QObject *source, const
//      QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection9setSourceEP7QObjectRK6QPoint(
    qdesigner_internal::Connection *self,
    QObject *source,
    const QPoint *pos) {
  self->setSource(source, *pos);
}

//  void qdesigner_internal::Connection::setTarget(QObject *target, const
//      QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection9setTargetEP7QObjectRK6QPoint(
    qdesigner_internal::Connection *self,
    QObject *target,
    const QPoint *pos) {
  self->setTarget(target, *pos);
}

//  void qdesigner_internal::Connection::updateKneeList()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection14updateKneeListEv(
    qdesigner_internal::Connection *self) {
  self->updateKneeList();
}

//  void qdesigner_internal::Connection::trimLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection8trimLineEv(
    qdesigner_internal::Connection *self) {
  self->trimLine();
}

//  void qdesigner_internal::Connection::updatePixmap(EndPoint::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10Connection12updatePixmapENS_7CETypes8EndPoint4TypeE(
    qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  self->updatePixmap(type);
}

//  LineDir qdesigner_internal::Connection::labelDir(EndPoint::Type type)
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::CETypes::LineDir ritual_ZNK18qdesigner_internal10Connection8labelDirENS_7CETypes8EndPoint4TypeE(
    const qdesigner_internal::Connection *self,
    qdesigner_internal::CETypes::EndPoint::Type type) {
  return self->labelDir(type);
}

//  bool qdesigner_internal::Connection::ground() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal10Connection6groundEv(
    const qdesigner_internal::Connection *self) {
  return self->ground();
}

//  QRect qdesigner_internal::Connection::groundRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal10Connection10groundRectEv(
    const qdesigner_internal::Connection *self) {
  return new QRect(self->groundRect());
}

//  a Python function taken by a Cuteqdesigner_internal_Connection, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_Connection(
    qdesigner_internal::Connection *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_Connection *>(self)->take(key, call);
}

//  void qdesigner_internal::Connection::updateVisibility()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal10Connection16updateVisibilityEv(
    qdesigner_internal::Connection *self) {
  self->qdesigner_internal::Connection::updateVisibility();
}

//  QRegion qdesigner_internal::Connection::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK18qdesigner_internal10Connection6regionEv(
    const qdesigner_internal::Connection *self) {
  return new QRegion(self->qdesigner_internal::Connection::region());
}

//  void qdesigner_internal::Connection::paint(QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18qdesigner_internal10Connection5paintEP8QPainter(
    const qdesigner_internal::Connection *self,
    QPainter *p) {
  self->qdesigner_internal::Connection::paint(p);
}

//  void qdesigner_internal::Connection::inserted()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal10Connection8insertedEv(
    qdesigner_internal::Connection *self) {
  self->qdesigner_internal::Connection::inserted();
}

//  void qdesigner_internal::Connection::removed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal10Connection7removedEv(
    qdesigner_internal::Connection *self) {
  self->qdesigner_internal::Connection::removed();
}
