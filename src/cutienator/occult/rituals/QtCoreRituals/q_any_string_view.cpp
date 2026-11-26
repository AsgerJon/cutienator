//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qanystringview.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qanystringview.h>
#include <QtCore/qchar.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qdebug.h>
#include <QtCore/qutf8stringview.h>

//  QChar QAnyStringView::toQChar(char ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN14QAnyStringView7toQCharEc(char ch) {
  return new QChar(QAnyStringView::toQChar(ch));
}

//  QChar QAnyStringView::toQChar(QChar ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN14QAnyStringView7toQCharE5QChar(const QChar *ch) {
  return new QChar(QAnyStringView::toQChar(*ch));
}

//  QChar QAnyStringView::toQChar(QLatin1Char ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN14QAnyStringView7toQCharE11QLatin1Char(
    const QLatin1Char *ch) {
  return new QChar(QAnyStringView::toQChar(*ch));
}

//  QAnyStringView::QAnyStringView(const void *d, qsizetype n, std::size_t
//      sizeAndType)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1EPKvxm(
    const void *d,
    qsizetype n,
    std::size_t sizeAndType) {
  return new QAnyStringView(d, n, sizeAndType);
}

//  QAnyStringView::QAnyStringView()
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1Ev() {
  return new QAnyStringView();
}

//  QAnyStringView::QAnyStringView(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1EDn() {
  return new QAnyStringView(nullptr);
}

//  QAnyStringView::QAnyStringView(const QByteArray &str)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1ERK10QByteArray(
    const QByteArray *str) {
  return new QAnyStringView(*str);
}

//  QAnyStringView::QAnyStringView(const QString &str)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1ERK7QString(const QString *str) {
  return new QAnyStringView(*str);
}

//  QAnyStringView::QAnyStringView(QLatin1StringView str)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1E13QLatin1String(
    const QLatin1String *str) {
  return new QAnyStringView(*str);
}

//  QAnyStringView::QAnyStringView(QStringView v)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringViewC1E11QStringView(const QString *v) {
  return new QAnyStringView(QStringView(*v));
}

//  QAnyStringView QAnyStringView::mid(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView3midExx(
    const QAnyStringView *self,
    qsizetype pos,
    qsizetype n) {
  return new QString(self->mid(pos, n).toString());
}

//  QAnyStringView QAnyStringView::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView4leftEx(
    const QAnyStringView *self,
    qsizetype n) {
  return new QString(self->left(n).toString());
}

//  QAnyStringView QAnyStringView::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView5rightEx(
    const QAnyStringView *self,
    qsizetype n) {
  return new QString(self->right(n).toString());
}

//  QAnyStringView QAnyStringView::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView6slicedEx(
    const QAnyStringView *self,
    qsizetype pos) {
  return new QString(self->sliced(pos).toString());
}

//  QAnyStringView QAnyStringView::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView6slicedExx(
    const QAnyStringView *self,
    qsizetype pos,
    qsizetype n) {
  return new QString(self->sliced(pos, n).toString());
}

//  QAnyStringView QAnyStringView::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView5firstEx(
    const QAnyStringView *self,
    qsizetype n) {
  return new QString(self->first(n).toString());
}

//  QAnyStringView QAnyStringView::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView4lastEx(
    const QAnyStringView *self,
    qsizetype n) {
  return new QString(self->last(n).toString());
}

//  QAnyStringView QAnyStringView::chopped(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView7choppedEx(
    const QAnyStringView *self,
    qsizetype n) {
  return new QString(self->chopped(n).toString());
}

//  QAnyStringView &QAnyStringView::slice(qsizetype pos)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringView5sliceEx(
    QAnyStringView *self,
    qsizetype pos) {
  return &(self->slice(pos));
}

//  QAnyStringView &QAnyStringView::slice(qsizetype pos, qsizetype n)
extern "C" Q_DECL_EXPORT
QAnyStringView *ritual_ZN14QAnyStringView5sliceExx(
    QAnyStringView *self,
    qsizetype pos,
    qsizetype n) {
  return &(self->slice(pos, n));
}

//  void QAnyStringView::truncate(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAnyStringView8truncateEx(
    QAnyStringView *self,
    qsizetype n) {
  self->truncate(n);
}

//  void QAnyStringView::chop(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAnyStringView4chopEx(QAnyStringView *self, qsizetype n) {
  self->chop(n);
}

//  QString QAnyStringView::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView8toStringEv(const QAnyStringView *self) {
  return new QString(self->toString());
}

//  qsizetype QAnyStringView::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QAnyStringView4sizeEv(const QAnyStringView *self) {
  return self->size();
}

//  const void *QAnyStringView::data() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK14QAnyStringView4dataEv(const QAnyStringView *self) {
  return self->data();
}

//  int QAnyStringView::compare(QAnyStringView lhs, QAnyStringView rhs,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAnyStringView7compareES_S_N2Qt15CaseSensitivityE(
    const QString *lhs,
    const QString *rhs,
    Qt::CaseSensitivity cs) {
  return QAnyStringView::compare(
      QAnyStringView(*lhs),
      QAnyStringView(*rhs),
      cs);
}

//  bool QAnyStringView::equal(QAnyStringView lhs, QAnyStringView rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QAnyStringView5equalES_S_(
    const QString *lhs,
    const QString *rhs) {
  return QAnyStringView::equal(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

//  QChar QAnyStringView::front() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK14QAnyStringView5frontEv(const QAnyStringView *self) {
  return new QChar(self->front());
}

//  QChar QAnyStringView::back() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK14QAnyStringView4backEv(const QAnyStringView *self) {
  return new QChar(self->back());
}

//  bool QAnyStringView::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAnyStringView5emptyEv(const QAnyStringView *self) {
  return self->empty();
}

//  qsizetype QAnyStringView::size_bytes() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QAnyStringView10size_bytesEv(
    const QAnyStringView *self) {
  return self->size_bytes();
}

//  qsizetype QAnyStringView::max_size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QAnyStringView8max_sizeEv(const QAnyStringView *self) {
  return self->max_size();
}

//  bool QAnyStringView::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAnyStringView6isNullEv(const QAnyStringView *self) {
  return self->isNull();
}

//  bool QAnyStringView::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAnyStringView7isEmptyEv(const QAnyStringView *self) {
  return self->isEmpty();
}

//  qsizetype QAnyStringView::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QAnyStringView6lengthEv(const QAnyStringView *self) {
  return self->length();
}

//  bool operator==(const QAnyStringView &lhs, const QAnyStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QAnyStringViewS1_(
    const QString *lhs,
    const QString *rhs) {
  return operator==(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

//  bool operator!=(const QAnyStringView &lhs, const QAnyStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QAnyStringViewS1_(
    const QString *lhs,
    const QString *rhs) {
  return operator!=(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

//  bool operator<(const QAnyStringView &lhs, const QAnyStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QAnyStringViewS1_(
    const QString *lhs,
    const QString *rhs) {
  return operator<(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

//  bool operator>(const QAnyStringView &lhs, const QAnyStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QAnyStringViewS1_(
    const QString *lhs,
    const QString *rhs) {
  return operator>(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

//  bool operator<=(const QAnyStringView &lhs, const QAnyStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QAnyStringViewS1_(
    const QString *lhs,
    const QString *rhs) {
  return operator<=(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

//  bool operator>=(const QAnyStringView &lhs, const QAnyStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QAnyStringViewS1_(
    const QString *lhs,
    const QString *rhs) {
  return operator>=(QAnyStringView(*lhs), QAnyStringView(*rhs));
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug d, QAnyStringView s)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebug14QAnyStringView(
    const QDebug *d,
    const QString *s) {
  return new QDebug(operator<<(*d, QAnyStringView(*s)));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  Tag QAnyStringView::tag() const
extern "C" Q_DECL_EXPORT
QAnyStringView::Tag ritual_ZNK14QAnyStringView3tagEv(
    const QAnyStringView *self) {
  return self->tag();
}

//  bool QAnyStringView::isUtf16() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAnyStringView7isUtf16Ev(const QAnyStringView *self) {
  return self->isUtf16();
}

//  bool QAnyStringView::isUtf8() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAnyStringView6isUtf8Ev(const QAnyStringView *self) {
  return self->isUtf8();
}

//  bool QAnyStringView::isLatin1() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAnyStringView8isLatin1Ev(const QAnyStringView *self) {
  return self->isLatin1();
}

//  QStringView QAnyStringView::asStringView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAnyStringView12asStringViewEv(
    const QAnyStringView *self) {
  return new QString(self->asStringView().toString());
}

//  q_no_char8_t::QUtf8StringView QAnyStringView::asUtf8StringView() const
extern "C" Q_DECL_EXPORT
q_no_char8_t::QUtf8StringView *ritual_ZNK14QAnyStringView16asUtf8StringViewEv(
    const QAnyStringView *self) {
  return new q_no_char8_t::QUtf8StringView(self->asUtf8StringView());
}

//  QLatin1StringView QAnyStringView::asLatin1StringView() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK14QAnyStringView18asLatin1StringViewEv(
    const QAnyStringView *self) {
  return new QLatin1String(self->asLatin1StringView());
}

//  size_t QAnyStringView::charSize() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK14QAnyStringView8charSizeEv(const QAnyStringView *self) {
  return self->charSize();
}

//  void QAnyStringView::setSize(qsizetype sz)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAnyStringView7setSizeEx(
    QAnyStringView *self,
    qsizetype sz) {
  self->setSize(sz);
}

//  void QAnyStringView::decreaseSize(qsizetype delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAnyStringView12decreaseSizeEx(
    QAnyStringView *self,
    qsizetype delta) {
  self->decreaseSize(delta);
}

//  void QAnyStringView::advanceData(qsizetype delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAnyStringView11advanceDataEx(
    QAnyStringView *self,
    qsizetype delta) {
  self->advanceData(delta);
}

//  void QAnyStringView::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QAnyStringView6verifyExx(
    const QAnyStringView *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}

//  QAnyStringView::~QAnyStringView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAnyStringViewD1Ev(QAnyStringView *self) {
  delete self;
}

//  a q_no_char8_t::QUtf8StringView a ritual of QAnyStringView gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAnyStringView__q_no_char8_t_QUtf8StringView(
    q_no_char8_t::QUtf8StringView *self) {
  delete self;
}

//  QAnyStringView::QAnyStringView<char, true>(const char *str, qsizetype
//      len)
extern "C" Q_DECL_EXPORT
QAnyStringView * ritual_ZN14QAnyStringViewC1IcLb1EEEPKcx(
    const char *str,
    qsizetype len) {
  return new QAnyStringView(str, len);
}

//  QAnyStringView::QAnyStringView<char16_t, true>(const char16_t *str,
//      qsizetype len)
extern "C" Q_DECL_EXPORT
QAnyStringView * ritual_ZN14QAnyStringViewC1IDsLb1EEEPKDsx(
    const char16_t *str,
    qsizetype len) {
  return new QAnyStringView(str, len);
}

//  QAnyStringView::QAnyStringView<const char *, true>(const char * const
//      &str)
extern "C" Q_DECL_EXPORT
QAnyStringView * ritual_ZN14QAnyStringViewC1IPKcLb1EEERKT_(
    const char *str) {
  return new QAnyStringView(str);
}

//  QAnyStringView::QAnyStringView<const char16_t *, true>(const char16_t *
//      const &str)
extern "C" Q_DECL_EXPORT
QAnyStringView * ritual_ZN14QAnyStringViewC1IPKDsLb1EEERKT_(
    const char16_t *str) {
  return new QAnyStringView(str);
}

//  QAnyStringView::QAnyStringView<false>(QBasicUtf8StringView<false> v)
extern "C" Q_DECL_EXPORT
QAnyStringView * ritual_ZN14QAnyStringViewC2ILb0EEE20QBasicUtf8StringViewIXT_EE(
    const QBasicUtf8StringView<false> *v) {
  return new QAnyStringView(*v);
}
