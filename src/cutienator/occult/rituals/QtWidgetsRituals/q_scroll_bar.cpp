//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qscrollbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qscrollbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QScrollBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QScrollBar10metaObjectEv(
    const QScrollBar *self) {
  return self->metaObject();
}

//  QString QScrollBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QScrollBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScrollBar::tr(s, c, n));
}

//  QScrollBar::QScrollBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZN10QScrollBarC1EP7QWidget(QWidget *parent) {
  return new QScrollBar(parent);
}

//  QScrollBar::QScrollBar(Qt::Orientation a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZN10QScrollBarC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation a0,
    QWidget *parent) {
  return new QScrollBar(a0, parent);
}

//  QScrollBar::~QScrollBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QScrollBarD1Ev(QScrollBar *self) {
  delete self;
}

//  QSize QScrollBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QScrollBar8sizeHintEv(const QScrollBar *self) {
  return new QSize(self->sizeHint());
}

//  bool QScrollBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QScrollBar5eventEP6QEvent(QScrollBar *self, QEvent *event) {
  return self->event(event);
}

//  QMenu *QScrollBar::createStandardContextMenu(QPoint position)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN10QScrollBar25createStandardContextMenuE6QPoint(
    QScrollBar *self,
    const QPoint *position) {
  return self->createStandardContextMenu(*position);
}
