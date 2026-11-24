//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QSvgTspan that Python can take functions over in. Every QSvgTspan
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgTspanCall0)(const void *, int *);
typedef bool (*CuteQSvgTspanCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgTspanCall2)(const void *, int *);
class CuteQSvgTspan : public QSvgTspan {
public:
  using QSvgTspan::QSvgTspan;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgTspan::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgTspanCall0 call = reinterpret_cast<CuteQSvgTspanCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgTspan::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgTspanCall1 call = reinterpret_cast<CuteQSvgTspanCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgTspanCall2 call = reinterpret_cast<CuteQSvgTspanCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgTspan::QSvgTspan(QSvgNode *parent, bool isProperTspan)
extern "C" Q_DECL_EXPORT
QSvgTspan *ritual_ZN9QSvgTspanC1EP8QSvgNodeb(
    QSvgNode *parent,
    bool isProperTspan) {
  return new CuteQSvgTspan(parent, isProperTspan);
}

//  QSvgTspan::~QSvgTspan()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgTspanD1Ev(QSvgTspan *self) {
  delete self;
}

//  Type QSvgTspan::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK9QSvgTspan4typeEv(const QSvgTspan *self) {
  return self->type();
}

//  void QSvgTspan::addText(QStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgTspan7addTextE11QStringView(
    QSvgTspan *self,
    const QString *text) {
  self->addText(QStringView(*text));
}

//  const QString &QSvgTspan::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSvgTspan4textEv(const QSvgTspan *self) {
  return new QString(self->text());
}

//  bool QSvgTspan::isTspan() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSvgTspan7isTspanEv(const QSvgTspan *self) {
  return self->isTspan();
}

//  void QSvgTspan::setWhitespaceMode(QSvgText::WhitespaceMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgTspan17setWhitespaceModeEN8QSvgText14WhitespaceModeE(
    QSvgTspan *self,
    QSvgText::WhitespaceMode mode) {
  self->setWhitespaceMode(mode);
}

//  QSvgText::WhitespaceMode QSvgTspan::whitespaceMode() const
extern "C" Q_DECL_EXPORT
QSvgText::WhitespaceMode ritual_ZNK9QSvgTspan14whitespaceModeEv(
    const QSvgTspan *self) {
  return self->whitespaceMode();
}

//  a Python function taken by a CuteQSvgTspan, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgTspan(QSvgTspan *self, const char *key, void *call) {
  return static_cast<CuteQSvgTspan *>(self)->take(key, call);
}

//  Type QSvgTspan::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK9QSvgTspan4typeEv(const QSvgTspan *self) {
  return self->QSvgTspan::type();
}

//  QList<QSvgTspan *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSvgTspan *> *ritual_list_make_QSvgTspan_ptr() {
  return new QList<QSvgTspan *>();
}

//  void QList<QSvgTspan *>::append(const QSvgTspan * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSvgTspan_ptr(
    QList<QSvgTspan *> *self,
    QSvgTspan *element) {
  self->append(element);
}

//  qsizetype QList<QSvgTspan *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSvgTspan_ptr(const QList<QSvgTspan *> *self) {
  return self->size();
}

//  const QSvgTspan * &QList<QSvgTspan *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSvgTspan *ritual_list_at_QSvgTspan_ptr(
    const QList<QSvgTspan *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSvgTspan *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSvgTspan_ptr(QList<QSvgTspan *> *self) {
  delete self;
}
