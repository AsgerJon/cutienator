//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandoutputmode.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandoutputmode.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>

//  QWaylandOutputMode::QWaylandOutputMode()
extern "C" Q_DECL_EXPORT
QWaylandOutputMode *ritual_ZN18QWaylandOutputModeC1Ev() {
  return new QWaylandOutputMode();
}

//  QWaylandOutputMode::QWaylandOutputMode(const QSize &size, int
//      refreshRate)
extern "C" Q_DECL_EXPORT
QWaylandOutputMode *ritual_ZN18QWaylandOutputModeC1ERK5QSizei(
    const QSize *size,
    int refreshRate) {
  return new QWaylandOutputMode(*size, refreshRate);
}

//  QWaylandOutputMode::QWaylandOutputMode(const QWaylandOutputMode &other)
extern "C" Q_DECL_EXPORT
QWaylandOutputMode *ritual_ZN18QWaylandOutputModeC1ERKS_(
    const QWaylandOutputMode *other) {
  return new QWaylandOutputMode(*other);
}

//  QWaylandOutputMode::~QWaylandOutputMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandOutputModeD1Ev(QWaylandOutputMode *self) {
  delete self;
}

//  bool QWaylandOutputMode::operator==(const QWaylandOutputMode &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWaylandOutputModeeqERKS_(
    const QWaylandOutputMode *self,
    const QWaylandOutputMode *other) {
  return self->operator==(*other);
}

//  bool QWaylandOutputMode::operator!=(const QWaylandOutputMode &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWaylandOutputModeneERKS_(
    const QWaylandOutputMode *self,
    const QWaylandOutputMode *other) {
  return self->operator!=(*other);
}

//  bool QWaylandOutputMode::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWaylandOutputMode7isValidEv(
    const QWaylandOutputMode *self) {
  return self->isValid();
}

//  QSize QWaylandOutputMode::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QWaylandOutputMode4sizeEv(
    const QWaylandOutputMode *self) {
  return new QSize(self->size());
}

//  int QWaylandOutputMode::refreshRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWaylandOutputMode11refreshRateEv(
    const QWaylandOutputMode *self) {
  return self->refreshRate();
}

//  void QWaylandOutputMode::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandOutputMode7setSizeERK5QSize(
    QWaylandOutputMode *self,
    const QSize *size) {
  self->setSize(*size);
}

//  QList<QWaylandOutputMode>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandOutputMode> *ritual_list_make_QWaylandOutputMode() {
  return new QList<QWaylandOutputMode>();
}

//  void QList<QWaylandOutputMode>::append(const QWaylandOutputMode &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandOutputMode(
    QList<QWaylandOutputMode> *self,
    const QWaylandOutputMode *element) {
  self->append(*element);
}

//  qsizetype QList<QWaylandOutputMode>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandOutputMode(
    const QList<QWaylandOutputMode> *self) {
  return self->size();
}

//  const QWaylandOutputMode &QList<QWaylandOutputMode>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QWaylandOutputMode *ritual_list_at_QWaylandOutputMode(
    const QList<QWaylandOutputMode> *self,
    long long index) {
  return new QWaylandOutputMode(self->at(index));
}

//  QList<QWaylandOutputMode>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandOutputMode(QList<QWaylandOutputMode> *self) {
  delete self;
}
